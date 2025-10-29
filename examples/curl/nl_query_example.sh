#!/bin/bash

# Natural Language Query (GET)
curl -sS "https://api.qoery.com/v0/query/nl?query=population%20of%20France&num_results=10&paragraph_extraction=false&plot2table=0" \
  -H "X-API-Key: YOUR_API_KEY"
