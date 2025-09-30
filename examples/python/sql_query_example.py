from qoery import Configuration, ApiClient, QueriesApi, SQLQueryRequest

configuration = Configuration()
configuration.host = 'https://api.qoery.com/v0'
configuration.api_key['ApiKeyAuth'] = 'your-api-key'

with ApiClient(configuration) as api_client:
    queries_api = QueriesApi(api_client)
    # Use 'query' field (sql_query is also supported for backward compatibility)
    request = SQLQueryRequest(query="SELECT date, value FROM emissions WHERE country = 'France' LIMIT 10")
    result = queries_api.query_sql_post(request)
    
    # Response includes: series, sql_query, metadata
    print(f"Executed SQL: {result.sql_query}")
    print(f"Series count: {len(result.series)}")
    for series in result.series:
        print(f"  {series.name}: {len(series.observations)} observations")
