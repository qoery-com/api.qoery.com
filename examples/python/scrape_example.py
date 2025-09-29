from openapi_client.api.data_sources_api import DataSourcesApi
from openapi_client.model.url_request import URLRequest
from openapi_client import Configuration, ApiClient

configuration = Configuration()
configuration.api_key['X-API-Key'] = 'your-api-key'
with ApiClient(configuration) as api_client:
    data_sources_api = DataSourcesApi(api_client)
    result = data_sources_api.scrape_post(URLRequest(url="https://example.com"))
