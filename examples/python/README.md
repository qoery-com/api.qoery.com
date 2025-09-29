# Python SDK Examples

This directory contains simple examples demonstrating how to use the qoery Python SDK for each API endpoint.

## Setup

1. Install the SDK:
```bash
pip install -e /path/to/sdks/python-sdk
```

2. Set your API key as an environment variable:
```bash
export QOERY_API_KEY="your-api-key-here"
```

Or replace `'your-api-key-here'` in each example file with your actual API key.

## Examples

### 1. Usage Statistics (`usage_example.py`)
Demonstrates how to get your current usage statistics and rate limits.

```bash
python usage_example.py
```

### 2. Natural Language Query (`nl_query_example.py`)
Shows how to query data using natural language. The API will convert your question into SQL and return time series data.

```bash
python nl_query_example.py
```

### 3. SQL Query (`sql_query_example.py`)
Demonstrates direct SQL query execution. You provide the SQL, and the API returns time series data.

```bash
python sql_query_example.py
```

### 4. Web Scraping (`scrape_example.py`)
Shows how to extract time series data from any URL containing tabular data.

```bash
python scrape_example.py
```

## API Endpoints

- **GET /usage** - Get usage statistics and rate limits
- **POST /query/nl** - Natural language to time series
- **POST /query/sql** - SQL to time series  
- **POST /scrape** - URL to time series

## Authentication

All endpoints require an API key passed in the `X-API-Key` header. Set your API key as an environment variable or modify the examples directly.

## Error Handling

Each example includes basic error handling. In production, you should implement more robust error handling based on your needs.

## Rate Limits

The API includes rate limiting headers in responses. Monitor these headers to stay within your limits:

- `X-RateLimit-Limit` - Maximum requests per time window
- `X-RateLimit-Remaining` - Requests remaining in current window
- `X-RateLimit-Reset` - Unix timestamp when rate limit resets
- `X-Concurrent-Limit` - Maximum concurrent requests allowed
- `X-Concurrent-Current` - Current concurrent requests
