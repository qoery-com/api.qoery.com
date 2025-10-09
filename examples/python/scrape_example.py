import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = "your-api-key"

with qoery.ApiClient(configuration) as api_client:
    api = qoery.WebScrapingApi(api_client)
    request = qoery.ScrapePostRequest(url="https://example.com/statistics")
    response = api.scrape_post(request)

