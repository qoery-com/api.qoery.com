// Usage via SDK (GET)
const Qoery = require('qoery');

const client = Qoery.ApiClient.instance;
const apiKeyAuth = client.authentications['ApiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR_API_KEY';

const usageApi = new Qoery.UsageApi();

usageApi.usageGet((error, data) => {
  if (error) {
    throw error;
  }
  console.log(data);
});
