import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = "your-api-key"

with qoery.ApiClient(configuration) as api_client:
    api = qoery.QueriesApi(api_client)
    request = qoery.QueryNlPostRequest(query="population of France")
    response = api.query_nl_post(request).to_dict()
    