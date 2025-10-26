import requests

# Example: Convert chart image to data table
url = "https://api.qoery.com/v0/plot2table"
params = {
    "image_url": "https://example.com/chart.png"
}
headers = {
    "X-API-Key": "YOUR_API_KEY"
}

response = requests.get(url, params=params, headers=headers)
print(response.json())
