import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

with qoery.ApiClient(configuration) as api_client:
    api = qoery.QueriesApi(api_client)
    data = api.query_nl_get(
        "population of France",
        num_results=10,
        paragraph_extraction=False,
        plot2table=0,
    )
    print(data)
    