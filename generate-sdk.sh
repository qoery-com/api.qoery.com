#!/bin/bash
set -euo pipefail

# Configurable settings (override via env vars when invoking the script)
VERSION=${VERSION:-0.2.0}
PY_PKG_NAME=${PY_PKG_NAME:-qoery}
PY_PROJECT_NAME=${PY_PROJECT_NAME:-qoery}
DESC_TXT=${DESC_TXT:-Every number on the internet, queryable.}
DESC_PROP=${DESC_TXT// /_}
PY_URL=${PY_URL:-https://github.com/qoery/python-sdk}
PY_AUTHOR=${PY_AUTHOR:-qoery_team}

NPM_NAME=${NPM_NAME:-qoery}
JS_PROJECT_NAME=${JS_PROJECT_NAME:-qoery}

# Generate Python SDK
openapi-generator-cli generate \
  -i api.yaml \
  -g python \
  -o ./sdks/python-sdk \
  --additional-properties=packageName=${PY_PKG_NAME},projectName=${PY_PROJECT_NAME},projectDescription=${DESC_PROP},packageUrl=${PY_URL},packageAuthor=${PY_AUTHOR},packageVersion=${VERSION}

echo "Python SDK generated successfully! (${PY_PKG_NAME} v${VERSION})"

# Generate JavaScript SDK
openapi-generator-cli generate \
  -i api.yaml \
  -g javascript \
  -o ./sdks/js \
  --additional-properties npmName=${NPM_NAME},projectName=${JS_PROJECT_NAME},npmVersion=${VERSION},projectDescription=${DESC_PROP}

echo "JS SDK generated successfully! (${NPM_NAME} v${VERSION})"
