const { QueriesApi, NLQueryRequest, ApiClient } = require('qoerys_api');

const apiClient = new ApiClient();
apiClient.defaultHeaders['X-API-Key'] = 'your-api-key';

const queriesApi = new QueriesApi(apiClient);
const result = queriesApi.queryNlPost(new NLQueryRequest({ query: "CO2 emissions for France" }));
