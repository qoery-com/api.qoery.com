from qoery import Configuration, ApiClient, WebScrapingApi, URLRequest

configuration = Configuration()
configuration.api_key['ApiKeyAuth'] = 'your-api-key'
with ApiClient(configuration) as api_client:
    scraping_api = WebScrapingApi(api_client)
    result = scraping_api.scrape_post(URLRequest(url="https://example.com"))
    print(result)
