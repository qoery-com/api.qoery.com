import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

with qoery.ApiClient(configuration) as api_client:
    api = qoery.PlansApi(api_client)
    plans = api.list_plans()
    print(f"Plans: {list(plans.plans.keys())}")
