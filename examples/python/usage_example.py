import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = "your-api-key"

with qoery.ApiClient(configuration) as api_client:
    api = qoery.UsageApi(api_client)
    response = api.usage_get(uid="00000000-0000-0000-0000-000000000000")
