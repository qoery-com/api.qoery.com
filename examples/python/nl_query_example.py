import requests

url = "https://api.qoery.com/v0/query/nl"
params = {
    "query": "population of France",
    "num_results": 10,
    "paragraph_extraction": False,
    "plot2table": 0,
}
headers = {"X-API-Key": "YOUR_API_KEY"}

resp = requests.get(url, params=params, headers=headers)
print(resp.json())
    