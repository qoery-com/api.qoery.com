#!/bin/bash

curl -X POST "https://api.qoery.com/v0/query/sql" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT date, value FROM emissions WHERE country = \"France\" LIMIT 10"}'
