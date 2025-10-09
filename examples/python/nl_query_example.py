import requests

response = requests.post(
    "https://api.qoery.com/v0/query/nl",
    headers={
        "X-API-Key": "your-api-key",
        "Content-Type": "application/json",
    },
    json={
        "query": "population of France"
    }
)

response.raise_for_status()
data = response.json()

print(f"Generated SQL: {data['sql_query']}")
print(f"Series returned: {len(data['series'])}")
print(f"Total results (meta.result_count): {data['meta']['result_count']}")
if data.get("description"):
    print(f"Description: {data['description']}")
