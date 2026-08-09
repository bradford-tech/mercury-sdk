# Mercury Python SDK

A generated Python client for the [Mercury API](https://docs.mercury.com/reference), built with
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

## Layout

| Path | What it is |
| --- | --- |
| `mercury-openapi.json` / `.yaml` | Source spec, hand-crawled from docs.mercury.com |
| `scripts/normalize_openapi.py` | Fixes spec patterns the generator can't consume |
| `mercury-openapi.normalized.json` | Generated input — do not edit by hand |
| `openapi-client-config.yaml` | Generator config (naming, content types, post-hooks) |
| `generate.sh` | Runs the whole pipeline |
| `mercury-sdk/` | The generated SDK — do not edit by hand |

## Regenerating

```bash
uv tool install openapi-python-client && uv tool install ruff
./generate.sh
```

`ruff` must be on `PATH` separately — the generator shells out to it for its post-generation
lint/format hooks.

To pick up API changes, re-crawl the spec (the docs expose
[llms.txt](https://docs.mercury.com/llms.txt)), overwrite `mercury-openapi.json`, and re-run
`./generate.sh`. The normalizer is deterministic and reports what it rewrote, so a re-crawl that
introduces a new spec pattern shows up as a `skipped` line rather than silently dropping schemas.

## Usage

```python
from mercury_sdk import AuthenticatedClient
from mercury_sdk.api.accounts import get_accounts
from mercury_sdk.api.transactions import list_transactions

# Mercury tokens include the "secret-token:" prefix; the client adds "Bearer ".
client = AuthenticatedClient(
    base_url="https://api.mercury.com/api/v1",
    token="secret-token:mercury_production_...",
)

with client as client:
    accounts = get_accounts.sync(client=client)
    for account in accounts.accounts:
        print(account.id, account.name, account.current_balance)

    txns = list_transactions.sync(client=client, limit=50)
    for txn in txns.transactions:
        print(txn.created_at, txn.amount, txn.counterparty_name)
```

Every endpoint module exposes four entry points:

- `sync()` — returns the parsed body, or `None`
- `sync_detailed()` — returns a `Response` with `status_code`, `content`, `headers`, `parsed`
- `asyncio()` / `asyncio_detailed()` — same, async

The API surface covers all 72 operations across 20 tags (Accounts, Cards, Transactions, Send Money,
Treasury, Invoices, Onboarding, Webhooks, OAuth2, and others).

## Spec normalization

Mercury's **published** OpenAPI uses `allOf: [{$ref: X}, {description: "..."}]` in 310 places to hang
a description off a `$ref` — this is upstream, not an artifact of the crawl, so it will be present in
every re-crawl and the normalizer is permanently required. That's valid OpenAPI, but
openapi-python-client treats any `allOf` as object composition and fails with *"Cannot take allOf a
non-object"* whenever `X` is a scalar or enum — which knocked out 43 schemas and every response
depending on them.

`scripts/normalize_openapi.py` rewrites each wrapper to an equivalent the generator accepts:

- **scalar target** (e.g. `UTCTime` → `string`): inline the target's keywords, keep the description.
  No class is generated for a scalar, so nothing is duplicated.
- **enum/object target**: rewrite to `oneOf: [{$ref: X}]`, which preserves `nullable` and
  `description` (siblings of a bare `$ref` are ignored in OpenAPI 3.0) while still pointing at the
  single shared generated class.

It also maps the spec's one non-standard format, `yyyy-mm-ddThh:MM:ssZ`, to `date-time`, so
timestamps arrive as `datetime.datetime`. All 41 uses are response-only — no request body or query
parameter carries that format — so this doesn't change anything the SDK sends.

Every `allOf` in the document matched the annotation-only pattern; there was no structural
composition to preserve.

## OAuth2 endpoints need a separate client

`GET /oauth2/auth` and `POST /oauth2/token` are published against a **different host**
(`https://oauth2.mercury.com`), which the spec correctly records as a path-level `servers` override.
openapi-python-client does not honour path-level `servers` — it emits a relative URL against the
client's `base_url` — so calling those two endpoints with your normal client hits the wrong host.

Use a dedicated client for them:

```python
from mercury_sdk import Client
from mercury_sdk.api.o_auth_2 import obtain_access_token

oauth_client = Client(base_url="https://oauth2.mercury.com")
token = obtain_access_token.sync(client=oauth_client, body=...)
```

The other 70 operations are correct against `https://api.mercury.com/api/v1`.

## Known gaps

Verified against the published docs — these are upstream gaps in Mercury's own OpenAPI, faithfully
reproduced by the spec, not crawl errors:

- `deleteCustomer` and `cancelInvoice` publish `"200": {"content": {"application/json": {}}}` — an
  empty schema — so they generate no typed response. The docs show no field table or example either,
  so the real shape can't be recovered from documentation; it needs a live call or Mercury support.
  The raw body is still available via `sync_detailed().content`.
- `startOAuth2Flow` responds `302` with `text/plain`; redirects aren't modeled as a parsed type.
- `uploadRecipientAttachment` / `uploadTransactionAttachment` declare a `200` with no body (the docs
  say in prose that they return `attachmentId` and `downloadUrl`, but publish no schema).
- Statement/invoice PDF endpoints are published as `application/pdf`; the generator skips content
  types it doesn't recognize, so `content_type_overrides` maps it to `application/octet-stream` and
  they return bytes.

## Verification

`scripts/verify_against_docs.py` re-checks the spec against Mercury's published OpenAPI. Each
`docs.mercury.com/reference/*.md` page embeds the authoritative OpenAPI JSON for its operation, so
the check is an exact structural diff — operation object plus its full transitive `$ref` closure —
rather than prose comparison, ignoring only annotation keys (`description`, `example`, ...).

```bash
python3 scripts/verify_against_docs.py          # fetches + diffs all 72 operations
python3 scripts/verify_against_docs.py --self-test   # mutation battery, proves the differ detects defects
```

As of the last run (2026-08-09): **72/72 operations byte-identical to the published spec**, and the
self-test caught 12/12 injected defects (added/removed enum value, added/removed `required` entry,
deleted property, wrong type, flipped `nullable`, removed parameter, renamed parameter, removed
status code, changed format, dropped OAuth2 `servers` override).

The check also compares the *effective server* per operation, resolving `servers` in OpenAPI order
(operation → path item → document root). That matters because each doc page is a one-operation
document declaring the override at its root, while our spec declares it path-level.

Four `llms.txt` reference entries (`cards`, `webhooks`, `events`, `accounts_receivable`) are
prose-only section overviews with no operation; the script reports them as skipped.
