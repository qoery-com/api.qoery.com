import requests

url = "https://api.qoery.com/v0/usage"
params = {"api_key": "YOUR_API_KEY"}
headers = {"X-API-Key": "YOUR_API_KEY"}

resp = requests.get(url, params=params, headers=headers)
print(resp.json())
