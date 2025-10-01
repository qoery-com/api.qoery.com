import requests

response = requests.post(
    "https://api.qoery.com/v0/query/sql",
    headers={"X-API-Key": "your-api-key"},
    json={"query": "SELECT * FROM series LIMIT 10"}
)

data = response.json()
print(f"Results: {len(data['series'])} observations")
