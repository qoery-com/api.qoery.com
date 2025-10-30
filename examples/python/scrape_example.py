import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

with qoery.ApiClient(configuration) as api_client:
    api = qoery.WebScrapingApi(api_client)
    data = api.scrape_get(
        url="https://example.com/statistics",
        paragraph_extraction=False,
        plot2table=0,
    )
    print(data)

