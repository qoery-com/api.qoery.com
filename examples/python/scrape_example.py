from qoery import Configuration, ApiClient, WebScrapingApi, URLRequest

configuration = Configuration()
configuration.host = 'https://api.qoery.com/v0'
configuration.api_key['ApiKeyAuth'] = 'your-api-key'

with ApiClient(configuration) as api_client:
    scraping_api = WebScrapingApi(api_client)
    request = URLRequest(url="https://example.com/statistics")
    # Use markdown=True and/or html=True query params to include content inline
    result = scraping_api.scrape_post(request, markdown=True)
    
    # Response includes: series, artifacts, cached (if from cache), source_id
    print(f"Cached: {result.cached if hasattr(result, 'cached') else False}")
    print(f"Series count: {len(result.series)}")
    if hasattr(result, 'markdown') and result.markdown:
        print(f"Markdown length: {len(result.markdown)} chars")
