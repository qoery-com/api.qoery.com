const { UsageApi, ApiClient } = require('qoerys_api');

const apiClient = new ApiClient();
apiClient.defaultHeaders['X-API-Key'] = 'your-api-key';

const usageApi = new UsageApi(apiClient);
const result = usageApi.usageGet();
