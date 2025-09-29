const { ApiClient, UsageApi } = require('qoery');

(async () => {
  const client = ApiClient.instance;
  client.basePath = 'https://api.qoery.com/v0';
  client.authentications['ApiKeyAuth'].apiKey = 'your-api-key';

  const usage = new UsageApi();
  const res = await usage.usageGet();
  console.log(res);
})();
