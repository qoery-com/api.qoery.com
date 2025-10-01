curl "https://api.qoery.com/v0/query/sql" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT * FROM series LIMIT 10"}'
