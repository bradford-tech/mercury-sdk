#!/usr/bin/env python3
"""Verify mercury-openapi.json against Mercury's published OpenAPI.

Each https://docs.mercury.com/reference/<slug>.md page embeds the authoritative
OpenAPI JSON for its operation under a "# OpenAPI definition" heading, including
the schemas that operation references. So this is not a prose comparison: for
every operation we diff the operation object plus its full transitive $ref
closure against our spec, ignoring only annotation keywords.

    python3 scripts/verify_against_docs.py
    python3 scripts/verify_against_docs.py --self-test

`--self-test` injects known defects one at a time and asserts each is detected,
so that a clean run means "no differences" rather than "the differ is broken".

Exit status is non-zero if any difference is found (usable in CI).
"""

from __future__ import annotations

import copy
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "mercury-openapi.json"
CACHE = ROOT / ".doc-cache"
INDEX_URL = "https://docs.mercury.com/llms.txt"
PAGE_URL = "https://docs.mercury.com/reference/{slug}.md"

# Purely descriptive — a difference here is not a correctness problem.
IGNORE = {
    "description",
    "example",
    "examples",
    "summary",
    "title",
    "externalDocs",
    "tags",
    "operationId",
    "deprecated",
}
METHODS = ("get", "post", "put", "patch", "delete")


def fetch(url: str, dest: Path) -> str:
    if dest.exists() and dest.stat().st_size:
        return dest.read_text()
    # docs.mercury.com 403s the default urllib User-Agent.
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        text = r.read().decode()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text)
    return text


def reference_slugs() -> list[str]:
    index = fetch(INDEX_URL, CACHE / "llms.txt")
    section = index.split("## API Reference", 1)[-1].split("\n## ", 1)[0]
    return re.findall(r"https://docs\.mercury\.com/reference/([^.]+)\.md", section)


def embedded_openapi(md_text: str) -> dict | None:
    i = md_text.find("# OpenAPI definition")
    if i < 0:
        return None
    m = re.search(r"```json\s*\n(.*?)\n```", md_text[i:], re.DOTALL)
    return json.loads(m.group(1)) if m else None


def norm(node):
    """Strip annotation keys and collapse single-$ref allOf/oneOf wrappers.
    Both sides use that wrapper, but not always in the same spot, so
    normalizing it keeps the diff focused on real structure."""
    if isinstance(node, dict):
        out = {k: norm(v) for k, v in node.items() if k not in IGNORE}
        for key in ("allOf", "oneOf"):
            members = out.get(key)
            if (
                isinstance(members, list)
                and len(members) == 1
                and isinstance(members[0], dict)
                and set(members[0]) == {"$ref"}
            ):
                ref = out.pop(key)[0]["$ref"]
                if not out:
                    return {"$ref": ref}
                out["$ref"] = ref
        return out
    if isinstance(node, list):
        return [norm(v) for v in node]
    return node


def closure(node, schemas, acc: set[str]) -> set[str]:
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
            name = ref.rsplit("/", 1)[-1]
            if name not in acc:
                acc.add(name)
                if name in schemas:
                    closure(schemas[name], schemas, acc)
        for v in node.values():
            closure(v, schemas, acc)
    elif isinstance(node, list):
        for v in node:
            closure(v, schemas, acc)
    return acc


def bundle(op_obj, schemas) -> dict:
    names = closure(op_obj, schemas, set())
    return {
        "op": norm(op_obj),
        "schemas": {
            n: norm(schemas.get(n, {"__MISSING__": True})) for n in sorted(names)
        },
    }


def deep_diff(spec_side, doc_side, path="", out=None) -> list[str]:
    if out is None:
        out = []
    if type(spec_side) is not type(doc_side):
        out.append(
            f"{path}: type {type(spec_side).__name__} vs {type(doc_side).__name__}"
        )
        return out
    if isinstance(spec_side, dict):
        for k in sorted(set(spec_side) | set(doc_side)):
            if k not in spec_side:
                out.append(
                    f"{path}/{k}: MISSING IN SPEC (docs have {json.dumps(doc_side[k])[:120]})"
                )
            elif k not in doc_side:
                out.append(
                    f"{path}/{k}: EXTRA IN SPEC ({json.dumps(spec_side[k])[:120]})"
                )
            else:
                deep_diff(spec_side[k], doc_side[k], f"{path}/{k}", out)
    elif isinstance(spec_side, list):
        if len(spec_side) != len(doc_side):
            out.append(
                f"{path}: length {len(spec_side)} vs {len(doc_side)} | "
                f"spec={json.dumps(spec_side)[:150]} docs={json.dumps(doc_side)[:150]}"
            )
        else:
            for i, (a, b) in enumerate(zip(spec_side, doc_side)):
                deep_diff(a, b, f"{path}/{i}", out)
    elif spec_side != doc_side:
        out.append(f"{path}: spec={json.dumps(spec_side)} docs={json.dumps(doc_side)}")
    return out


def effective_server(root: dict, path_item: dict, operation: dict) -> str | None:
    """OpenAPI server resolution: operation > path item > document root."""
    for level in (operation, path_item, root):
        servers = level.get("servers")
        if servers:
            return servers[0].get("url", "").rstrip("/")
    return None


def compare(spec: dict, pages: dict[str, dict]) -> tuple[dict[str, list[str]], int]:
    findings: dict[str, list[str]] = {}
    checked = 0
    for slug, doc in pages.items():
        doc_schemas = doc.get("components", {}).get("schemas", {})
        diffs: list[str] = []
        for p, ops in doc.get("paths", {}).items():
            spec_path = spec["paths"].get(p, {})
            for m, op in ops.items():
                if m not in METHODS:
                    continue
                checked += 1
                if m not in spec_path:
                    diffs.append(f"{m.upper()} {p}: OPERATION MISSING IN SPEC")
                    continue
                # Compare the *effective* server. A doc page is a one-operation
                # document that puts the override at its root, while our spec
                # puts it path-level; both resolve to the same host, and that
                # is what actually matters (the OAuth2 endpoints live off-host).
                doc_server = effective_server(doc, ops, op)
                spec_server = effective_server(spec, spec_path, spec_path[m])
                if doc_server != spec_server:
                    diffs.append(
                        f"{m.upper()} {p}/servers: spec={spec_server} docs={doc_server}"
                    )
                diffs += deep_diff(
                    bundle(spec_path[m], spec["components"]["schemas"]),
                    bundle(op, doc_schemas),
                    f"{m.upper()} {p}",
                )
        if diffs:
            findings[slug] = diffs
    return findings, checked


MUTATIONS = {
    "enum: add value": lambda s: s["components"]["schemas"]["TransactionStatus"][
        "enum"
    ].append("zzz"),
    "enum: remove value": lambda s: s["components"]["schemas"]["TransactionStatus"][
        "enum"
    ].pop(),
    "required: add entry": lambda s: s["components"]["schemas"]["Account"][
        "required"
    ].append("nickname"),
    "required: remove entry": lambda s: s["components"]["schemas"]["Account"][
        "required"
    ].pop(),
    "property: delete": lambda s: s["components"]["schemas"]["Account"][
        "properties"
    ].pop("accountNumber"),
    "property: wrong type": lambda s: s["components"]["schemas"]["Account"][
        "properties"
    ]["accountNumber"].__setitem__("type", "integer"),
    "nullable: flip": lambda s: s["components"]["schemas"]["Account"]["properties"][
        "nickname"
    ].__setitem__("nullable", False),
    "param: remove": lambda s: s["paths"]["/accounts"]["get"]["parameters"].pop(),
    "param: rename": lambda s: s["paths"]["/accounts"]["get"]["parameters"][
        0
    ].__setitem__("name", "limitX"),
    "status code: remove": lambda s: s["paths"]["/accounts"]["get"]["responses"].pop(
        "400", None
    ),
    "format: change": lambda s: s["components"]["schemas"][
        "TransactionPartyId"
    ].__setitem__("format", "int64"),
    "servers: drop oauth2 override": lambda s: s["paths"]["/oauth2/token"].pop(
        "servers"
    ),
}


def main() -> int:
    spec = json.loads(SPEC_PATH.read_text())
    slugs = reference_slugs()
    pages, overviews = {}, []
    for slug in slugs:
        doc = embedded_openapi(fetch(PAGE_URL.format(slug=slug), CACHE / f"{slug}.md"))
        if doc is None:
            # Section overviews (cards, webhooks, events, accounts_receivable)
            # are prose only and define no operation.
            overviews.append(slug)
            continue
        pages[slug] = doc
    if overviews:
        print(
            f"skipped {len(overviews)} prose-only overview pages: {', '.join(overviews)}"
        )

    if "--self-test" in sys.argv:
        caught = 0
        for name, mutate in MUTATIONS.items():
            mutated = copy.deepcopy(spec)
            try:
                mutate(mutated)
            except (KeyError, IndexError, TypeError) as exc:
                # The mutation targets a specific field; if the spec changed
                # shape, skip rather than reporting a false "MISSED".
                print(f"  SKIP    {name}: {exc!r}")
                continue
            findings, _ = compare(mutated, pages)
            detected = bool(findings)
            caught += detected
            print(f"  {'CAUGHT' if detected else 'MISSED':6s}  {name}")
        print(f"\n{caught}/{len(MUTATIONS)} injected defects detected")
        return 0 if caught == len(MUTATIONS) else 1

    findings, checked = compare(spec, pages)
    print(f"pages: {len(pages)}   operations compared: {checked}")
    print(f"pages with differences: {len(findings)}")
    for slug, diffs in sorted(findings.items()):
        print(f"\n=== {slug} ({len(diffs)}) ===")
        for d in diffs[:25]:
            print("   ", d)
        if len(diffs) > 25:
            print(f"    ... +{len(diffs) - 25} more")
    if not findings:
        print("\nSpec matches the published documentation exactly.")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
