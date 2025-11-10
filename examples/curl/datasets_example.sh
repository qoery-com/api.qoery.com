#!/bin/bash

# Start job
curl -X POST "https://api.qoery.com/v0/datasets?api_key=YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search": "climate change"}'
