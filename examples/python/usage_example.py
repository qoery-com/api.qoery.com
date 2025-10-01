import requests

response = requests.get(
    "https://api.qoery.com/v0/usage",
    headers={"X-API-Key": "your-api-key"},
    params={"uid": "your-user-id"}
)

data = response.json()
print(f"Plan: {data['plan']}")
print(f"NL calls: {data['endpoints']['nl']['calls_used']}/{data['endpoints']['nl']['calls_limit']}")
print(f"SQL calls: {data['endpoints']['sql']['calls_used']}/{data['endpoints']['sql']['calls_limit']}")
print(f"Scrape calls: {data['endpoints']['scrape']['calls_used']}/{data['endpoints']['scrape']['calls_limit']}")
