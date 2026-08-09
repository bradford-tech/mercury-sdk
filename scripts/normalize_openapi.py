#!/usr/bin/env python3
"""Normalize the Mercury OpenAPI document for openapi-python-client.

The Mercury spec uses `allOf: [{$ref: X}, {description: ...}]` in 310 places as a
way to attach a description (and sometimes `nullable`) to a `$ref`. That is legal
OpenAPI, but openapi-python-client treats any schema containing `allOf` as an
object-composition and fails with "Cannot take allOf a non-object" whenever the
referenced schema is a scalar or an enum. That single pattern is what knocks out
43 schemas (Transaction, Card, UserDetails, ...) and every endpoint response that
depends on them.

Every `allOf` in the document is this pattern -- exactly one `$ref` plus members
that carry annotation keywords only. There is no structural composition to
preserve, so each one is rewritten to an equivalent form the generator handles:

  * `$ref` to a plain scalar (e.g. UTCTime -> string/date-time): inline the
    target's keywords and layer the annotations on top. No class is generated for
    a scalar, so nothing is duplicated and the description survives.
  * `$ref` to an enum/object/union: rewrite to `oneOf: [{$ref: X}]` carrying the
    annotations. A single-member `oneOf` keeps the shared generated class (rather
    than allOf's inline copy of the merged properties) and lets `nullable` and
    `description` survive, which siblings of a bare `$ref` would not.

It also maps the one non-standard `format` in the document,
`yyyy-mm-ddThh:MM:ssZ`, to the standard `date-time`, so those fields come back as
`datetime.datetime` instead of `str`. All 41 uses are response-only -- no request
body or parameter carries this format -- so this cannot change what the SDK sends
to Mercury.

Usage: python3 scripts/normalize_openapi.py [input.json] [output.json]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

# Keywords that only annotate a schema -- they never change its shape.
ANNOTATION_KEYS = {
    "description",
    "title",
    "example",
    "examples",
    "deprecated",
    "readOnly",
    "writeOnly",
    "externalDocs",
    "default",
    "xml",
    "nullable",
}

# The crawled document spells RFC3339 timestamps with a human-readable format
# string that no generator recognizes. Response-only, so remapping is read-side.
NONSTANDARD_FORMATS = {"yyyy-mm-ddThh:MM:ssZ": "date-time"}


class Normalizer:
    def __init__(self, doc: dict[str, Any]) -> None:
        self.doc = doc
        self.schemas: dict[str, Any] = doc.get("components", {}).get("schemas", {})
        self.rewritten_scalar = 0
        self.rewritten_ref = 0
        self.rewritten_format = 0
        self.skipped: list[str] = []

    def resolve(self, ref: str) -> dict[str, Any] | None:
        """Follow a local component ref, including ref-to-ref chains."""
        seen: set[str] = set()
        while True:
            if not ref.startswith("#/components/schemas/"):
                return None
            name = ref.rsplit("/", 1)[-1]
            if name in seen:
                return None
            seen.add(name)
            target = self.schemas.get(name)
            if target is None:
                return None
            if "$ref" in target:
                ref = target["$ref"]
                continue
            return target

    @staticmethod
    def is_plain_scalar(target: dict[str, Any]) -> bool:
        if "enum" in target or "const" in target:
            return False
        if any(k in target for k in ("properties", "allOf", "oneOf", "anyOf", "items")):
            return False
        return target.get("type") in ("string", "number", "integer", "boolean")

    def rewrite(self, node: dict[str, Any], path: str) -> dict[str, Any]:
        """Rewrite a single annotation-only allOf node; return it unchanged if it
        is real composition."""
        members = node["allOf"]
        if not isinstance(members, list):
            return node

        refs = [m for m in members if isinstance(m, dict) and "$ref" in m]
        others = [m for m in members if isinstance(m, dict) and "$ref" not in m]
        other_keys: set[str] = set()
        for other in others:
            other_keys |= set(other.keys())

        # Anything but "one $ref plus annotations" is genuine composition: leave
        # it for the generator to merge as it already does correctly.
        if len(refs) != 1 or not other_keys <= ANNOTATION_KEYS:
            self.skipped.append(path)
            return node

        annotations: dict[str, Any] = {}
        for other in others:
            annotations.update(other)
        # Keys on the allOf node itself are more specific than the members'.
        annotations.update({k: v for k, v in node.items() if k != "allOf"})

        ref = refs[0]["$ref"]
        target = self.resolve(ref)

        if target is not None and self.is_plain_scalar(target):
            self.rewritten_scalar += 1
            return {**target, **annotations}

        self.rewritten_ref += 1
        if not annotations:
            return {"$ref": ref}
        return {"oneOf": [{"$ref": ref}], **annotations}

    def walk(self, node: Any, path: str = "") -> Any:
        if isinstance(node, dict):
            node = {k: self.walk(v, f"{path}/{k}") for k, v in node.items()}
            if "allOf" in node:
                node = self.rewrite(node, path)
            return node
        if isinstance(node, list):
            return [self.walk(v, f"{path}/{i}") for i, v in enumerate(node)]
        return node

    def fix_formats(self, node: Any) -> Any:
        """Second pass. Inlining above copies keywords out of the *original*
        schema dict, so formats must be remapped after that has settled or the
        inlined copies keep the non-standard spelling."""
        if isinstance(node, dict):
            node = {k: self.fix_formats(v) for k, v in node.items()}
            fmt = node.get("format")
            if isinstance(fmt, str) and fmt in NONSTANDARD_FORMATS:
                self.rewritten_format += 1
                return {**node, "format": NONSTANDARD_FORMATS[fmt]}
            return node
        if isinstance(node, list):
            return [self.fix_formats(v) for v in node]
        return node

    def run(self) -> dict[str, Any]:
        return self.fix_formats(self.walk(self.doc))


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "mercury-openapi.json"
    dst = (
        Path(sys.argv[2])
        if len(sys.argv) > 2
        else root / "mercury-openapi.normalized.json"
    )

    doc = json.loads(src.read_text())
    normalizer = Normalizer(doc)
    out = normalizer.run()

    # The rewrite is only valid if nothing structural is left behind.
    remaining = json.dumps(out).count('"allOf"')
    dst.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")

    print(f"read    {src}")
    print(f"wrote   {dst}")
    print(f"inlined {normalizer.rewritten_scalar} scalar-ref allOf wrappers")
    print(f"reftype {normalizer.rewritten_ref} enum/object-ref allOf wrappers -> oneOf")
    print(f"formats {normalizer.rewritten_format} non-standard formats -> date-time")
    print(f"skipped {len(normalizer.skipped)} genuine allOf compositions")
    for path in normalizer.skipped:
        print(f"        {path}")
    print(f"allOf occurrences remaining in output: {remaining}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
