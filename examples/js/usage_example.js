const Qoery = require('qoery');

const client = Qoery.ApiClient.instance;
client.authentications['ApiKeyAuth'].apiKey = 'YOUR_API_KEY';

const api = new Qoery.UsageApi();

api.getUsageStats({}, (error, usage) => {
  if (error) throw error;
  console.log(`Plan: ${usage.plan}, Usage: ${usage.total_usage}`);
});
