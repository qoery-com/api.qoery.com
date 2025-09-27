# Qoery API - Modular OpenAPI Specification

This repository contains the modular OpenAPI 3.1 specification for the Qoery API, organized in a standardized folder structure for better maintainability and organization.

## 📁 Standardized File Structure

```
api.qoery.com/
├── api.yaml                    # Main API specification with references
├── schemas/
│   └── schemas.yaml            # Shared data schemas and models
├── responses/
│   └── responses.yaml          # Reusable response definitions
├── paths/
│   ├── auth.yaml              # Authentication endpoints
│   ├── usage.yaml             # Usage statistics and rate limiting
│   ├── queries.yaml           # Query execution endpoints
│   └── data-sources.yaml      # Data source and scraping endpoints
└── README.md                  # This file
```

## 🏗️ Modular Architecture

### **Main API File (`api.yaml`)**
- Contains the main OpenAPI specification
- Defines global configuration (servers, security schemes, tags)
- References all module files using `$ref`

### **Schemas Folder (`schemas/`)**
- **`schemas.yaml`** - All shared data models and schemas
- Request/response models
- Reusable across all endpoints

### **Responses Folder (`responses/`)**
- **`responses.yaml`** - Common response definitions
- Error responses (401, 429, etc.)
- Rate limiting headers

### **Paths Folder (`paths/`)**
- **`auth.yaml`** - API key management endpoints
- **`usage.yaml`** - Usage statistics and monitoring
- **`queries.yaml`** - Natural language and SQL query processing
- **`data-sources.yaml`** - Web scraping and data extraction

## 🔧 Benefits of Modular Structure

1. **Separation of Concerns**: Each module focuses on a specific domain
2. **Maintainability**: Easier to update individual modules
3. **Team Collaboration**: Different teams can work on different modules
4. **Reusability**: Shared schemas and responses reduce duplication
5. **Scalability**: Easy to add new modules as the API grows

## 🚀 Usage

The main `api.yaml` file can be used with any OpenAPI-compatible tool:

```bash
# Validate the API specification
swagger-codegen validate -i api.yaml

# Generate client SDKs
swagger-codegen generate -i api.yaml -l python -o ./client

# Generate server stubs
swagger-codegen generate -i api.yaml -l nodejs-express -o ./server
```

## 📋 API Modules Overview

| Module | File | Endpoints | Purpose |
|--------|------|-----------|---------|
| **Authentication** | `paths/auth.yaml` | `/auth/keys` | API key management |
| **Usage** | `paths/usage.yaml` | `/usage` | Usage statistics and limits |
| **Queries** | `paths/queries.yaml` | `/query/nl`, `/query/sql` | Data querying |
| **Data Sources** | `paths/data-sources.yaml` | `/scrape` | Web scraping |

## 🔐 Security

All endpoints (except API key creation) require authentication via the `X-API-Key` header.

## 📊 Rate Limiting

All endpoints include comprehensive rate limiting headers:
- `X-RateLimit-Limit` - Maximum requests per window
- `X-RateLimit-Remaining` - Requests remaining
- `X-RateLimit-Reset` - Reset timestamp
- `X-Concurrent-Limit` - Concurrent request limits

## 🛠️ Development

To modify the API:

1. **Add new endpoints**: Create or update the relevant file in `paths/` folder
2. **Add new schemas**: Update `schemas/schemas.yaml`
3. **Add new responses**: Update `responses/responses.yaml`
4. **Update main API**: Modify `api.yaml` if needed

The standardized folder structure makes it easy to maintain and extend the API specification while keeping it organized and manageable.
