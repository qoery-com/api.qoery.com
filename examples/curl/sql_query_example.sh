#!/bin/bash

curl -X POST "https://api.qoery.com/query/sql" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"sql_query": "SELECT * FROM emissions"}'
