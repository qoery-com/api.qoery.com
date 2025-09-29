#!/bin/bash

curl -X POST "https://api.qoery.com/scrape" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
