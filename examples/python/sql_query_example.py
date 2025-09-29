from openapi_client.api.queries_api import QueriesApi
from openapi_client.model.sql_query_request import SQLQueryRequest
from openapi_client import Configuration, ApiClient

configuration = Configuration()
configuration.api_key['X-API-Key'] = 'your-api-key'
with ApiClient(configuration) as api_client:
    queries_api = QueriesApi(api_client)
    result = queries_api.query_sql_post(SQLQueryRequest(sql_query="SELECT * FROM emissions"))
