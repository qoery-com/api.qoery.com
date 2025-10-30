import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

with qoery.ApiClient(configuration) as api_client:
    api = qoery.WebScrapingApi(api_client)
    data = api.plot2table_get(image_url="https://example.com/chart.png")
    print(data)
