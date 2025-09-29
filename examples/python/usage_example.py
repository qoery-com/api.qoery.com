from qoery import Configuration, ApiClient, UsageApi

configuration = Configuration()
configuration.api_key['ApiKeyAuth'] = 'your-api-key'
with ApiClient(configuration) as api_client:
    usage_api = UsageApi(api_client)
    result = usage_api.usage_get()
    print(result)
