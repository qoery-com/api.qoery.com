import requests

response = requests.get(
    "https://api.qoery.com/v0/usage",
    headers={
        "X-API-Key": "your-api-key"
    },
    params={
        "uid": "00000000-0000-0000-0000-000000000000"
    }
)

response.raise_for_status()
data = response.json()

print(f"Plan: {data['plan']}")
print(f"Period: {data['period_start']} -> {data['period_end']}")
print(f"NL calls: {data['endpoints']['nl']['calls_used']}/{data['endpoints']['nl']['calls_limit']} (remaining: {data['endpoints']['nl']['remaining']})")
print(f"SQL calls: {data['endpoints']['sql']['calls_used']}/{data['endpoints']['sql']['calls_limit']} (remaining: {data['endpoints']['sql']['remaining']})")
print(f"Scrape calls: {data['endpoints']['scrape']['calls_used']}/{data['endpoints']['scrape']['calls_limit']} (remaining: {data['endpoints']['scrape']['remaining']})")
