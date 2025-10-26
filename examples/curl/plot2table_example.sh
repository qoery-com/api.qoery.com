#!/bin/bash

# Example: Convert chart image to data table
curl -X GET "https://api.qoery.com/v0/plot2table?image_url=https://example.com/chart.png" \
  -H "X-API-Key: YOUR_API_KEY"
