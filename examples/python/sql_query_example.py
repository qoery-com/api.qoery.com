from qoery import Configuration, ApiClient, QueriesApi, SQLQueryRequest

configuration = Configuration()
configuration.api_key['ApiKeyAuth'] = 'your-api-key'
with ApiClient(configuration) as api_client:
    queries_api = QueriesApi(api_client)
    result = queries_api.query_sql_post(SQLQueryRequest(sql="SELECT * FROM emissions"))
    print(result)
