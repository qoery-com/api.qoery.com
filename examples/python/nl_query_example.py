from qoery import Configuration, ApiClient, QueriesApi, NLQueryRequest

configuration = Configuration()
configuration.host = 'https://api.qoery.com/v0'
configuration.api_key['ApiKeyAuth'] = 'your-api-key'

with ApiClient(configuration) as api_client:
    queries_api = QueriesApi(api_client)
    request = NLQueryRequest(query="CO2 emissions for France from 2010 to 2020")
    result = queries_api.query_nl_post(request)
    
    # Response includes: sql_query, series, metadata, description
    print(f"Generated SQL: {result.sql_query}")
    print(f"Series count: {len(result.series)}")
    for series in result.series:
        print(f"  {series.name}: {len(series.observations)} observations")
