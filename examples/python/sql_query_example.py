import qoery

configuration = qoery.Configuration()
configuration.api_key['ApiKeyAuth'] = "your-api-key"

with qoery.ApiClient(configuration) as api_client:
    api = qoery.QueriesApi(api_client)
    request = qoery.QuerySqlPostRequest(query="SELECT * FROM series LIMIT 10")
    response = api.query_sql_post(request).to_dict()
    