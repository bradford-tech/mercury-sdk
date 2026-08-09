#!/usr/bin/env bash
# Regenerate the Mercury Python SDK from the OpenAPI document.
#
#   ./generate.sh
#
# Requires openapi-python-client and ruff on PATH:
#   uv tool install openapi-python-client && uv tool install ruff
# (ruff is what the generator's post-hooks use to lint/format the output.)
set -euo pipefail

cd "$(dirname "$0")"

SPEC="mercury-openapi.json"
NORMALIZED="mercury-openapi.normalized.json"
OUT="mercury-sdk"

# The spec is crawled from docs.mercury.com and uses `allOf: [$ref, {description}]`
# wrappers that openapi-python-client cannot process. Normalize first -- without
# this, 43 schemas (Transaction, Card, UserDetails, ...) are silently dropped.
python3 scripts/normalize_openapi.py "$SPEC" "$NORMALIZED"

openapi-python-client generate \
  --path "$NORMALIZED" \
  --config openapi-client-config.yaml \
  --output-path "$OUT" \
  --overwrite

echo
echo "Generated $OUT"
