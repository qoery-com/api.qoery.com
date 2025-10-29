#!/bin/bash

# Structured Web Scrape (GET)
curl -sS "https://api.qoery.com/v0/scrape?url=https%3A%2F%2Fexample.com%2Fstatistics&paragraph_extraction=false&plot2table=0" \
  -H "X-API-Key: YOUR_API_KEY"
