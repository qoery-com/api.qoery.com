from qoery import Configuration, ApiClient, UsageApi

configuration = Configuration()
configuration.host = 'https://api.qoery.com/v0'
configuration.api_key['ApiKeyAuth'] = 'your-api-key'

with ApiClient(configuration) as api_client:
    usage_api = UsageApi(api_client)
    result = usage_api.usage_get()
    
    # Response includes usage stats and token consumption
    print(f"Queries: {result.queries_used}/{result.queries_limit}")
    print(f"Tokens in: {result.tokens_in}, out: {result.tokens_out}")
    print(f"Errors: {result.errors}")
    print(f"Period: {result.period_start} to {result.period_end}")
