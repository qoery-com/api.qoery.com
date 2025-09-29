from openapi_client.api.usage_api import UsageApi
from openapi_client import Configuration, ApiClient

configuration = Configuration()
configuration.api_key['X-API-Key'] = 'your-api-key'
with ApiClient(configuration) as api_client:
    usage_api = UsageApi(api_client)
    result = usage_api.usage_get()
