import requests

response = requests.post(
    "https://api.qoery.com/v0/scrape",
    headers={"X-API-Key": "your-api-key"},
    json={"url": "https://example.com/statistics"}
)

data = response.json()
print(f"Cached: {data.get('cached', False)}")
print(f"Results: {len(data['series'])} observations")
