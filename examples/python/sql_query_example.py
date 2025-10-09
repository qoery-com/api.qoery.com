import requests

response = requests.post(
    "https://api.qoery.com/v0/query/sql",
    headers={
        "X-API-Key": "your-api-key",
        "Content-Type": "application/json",
    },
    json={
        "query": "SELECT * FROM series LIMIT 10"
    }
)

response.raise_for_status()
data = response.json()

print(f"Executed SQL: {data['sql_query']}")
print(f"Series returned: {len(data['series'])}")
print(f"Total results (meta.result_count): {data['meta']['result_count']}")
