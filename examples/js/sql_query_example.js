const { QueriesApi, SQLQueryRequest, ApiClient } = require('qoerys_api');

const apiClient = new ApiClient();
apiClient.defaultHeaders['X-API-Key'] = 'your-api-key';

const queriesApi = new QueriesApi(apiClient);
const result = queriesApi.querySqlPost(new SQLQueryRequest({ sqlQuery: "SELECT * FROM emissions" }));
