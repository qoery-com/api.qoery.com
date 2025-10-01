import requests

response = requests.post(
    "https://api.qoery.com/v0/query/nl",
    headers={"X-API-Key": "your-api-key"},
    json={"query": "population of France"}
)

data = response.json()
print(f"Generated SQL: {data['sql_query']}")
print(f"Results: {len(data['series'])} observations")
