import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

with qoery.ApiClient(configuration) as api_client:
    api = qoery.UsageApi(api_client)
    usage = api.get_usage_stats()
    print(f"Plan: {usage.plan}, Usage: {usage.total_usage}")
