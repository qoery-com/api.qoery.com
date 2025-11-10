import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

with qoery.ApiClient(configuration) as api_client:
    api = qoery.UsageApi(api_client)
    usage = api.v0_usage_get()
    print(f"Plan: {usage.plan}, Usage: {usage.total_usage}")
