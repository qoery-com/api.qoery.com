const { DataSourcesApi, URLRequest, ApiClient } = require('qoerys_api');

const apiClient = new ApiClient();
apiClient.defaultHeaders['X-API-Key'] = 'your-api-key';

const dataSourcesApi = new DataSourcesApi(apiClient);
const result = dataSourcesApi.scrapePost(new URLRequest({ url: "https://example.com" }));
