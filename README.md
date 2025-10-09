# Qoery API Documentation

Beautiful, interactive API documentation generated from OpenAPI 3.1 specification.

## 🚀 Quick Start

### Build the docs (Redoc)

```bash
python build_docs.py
```

This injects examples into the OpenAPI, builds `index.html` with Redoc, and writes it to the repo root.

### Generate SDKs

```bash
./generate-sdk.sh
```

Generates the JavaScript and Python SDKs from the current `api.yaml`.
