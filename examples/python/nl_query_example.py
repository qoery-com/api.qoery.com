from qoery import Configuration, ApiClient, QueriesApi, NLQueryRequest

configuration = Configuration()
configuration.api_key['ApiKeyAuth'] = 'your-api-key'
with ApiClient(configuration) as api_client:
    queries_api = QueriesApi(api_client)
    result = queries_api.query_nl_post(NLQueryRequest(query="CO2 emissions for France"))
    print(result)
