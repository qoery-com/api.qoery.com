const { ApiClient, UsageApi } = require('qoery');

(async () => {
  const client = ApiClient.instance;
  client.basePath = 'https://api.qoery.com/v0';
  client.authentications['ApiKeyAuth'].apiKey = 'your-api-key';

  const usage = new UsageApi();
  const res = await usage.usageGet();
  
  // Response includes usage stats and token consumption
  console.log(`Queries: ${res.queries_used}/${res.queries_limit}`);
  console.log(`Tokens in: ${res.tokens_in}, out: ${res.tokens_out}`);
  console.log(`Errors: ${res.errors}`);
  console.log(`Period: ${res.period_start} to ${res.period_end}`);
})();
