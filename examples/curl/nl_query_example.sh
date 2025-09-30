#!/bin/bash

curl -X POST "https://api.qoery.com/v0/query/nl" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"query": "CO2 emissions for France from 2010 to 2020"}'
