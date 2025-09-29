from openapi_client.api.queries_api import QueriesApi
from openapi_client.model.nl_query_request import NLQueryRequest
from openapi_client import Configuration, ApiClient

configuration = Configuration()
configuration.api_key['X-API-Key'] = 'your-api-key'
with ApiClient(configuration) as api_client:
    queries_api = QueriesApi(api_client)
    result = queries_api.query_nl_post(NLQueryRequest(query="CO2 emissions for France"))
