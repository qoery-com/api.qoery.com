#!/bin/bash

curl "https://api.qoery.com/v0/scrape" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/statistics"}'
