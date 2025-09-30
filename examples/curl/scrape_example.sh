#!/bin/bash

curl -X POST "https://api.qoery.com/v0/scrape?markdown=true" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/statistics"}'
