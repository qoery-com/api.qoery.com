const { ApiClient, QueriesApi, NLQueryRequest } = require('qoery');

(async () => {
  const client = ApiClient.instance;
  client.basePath = 'https://api.qoery.com/v0'; // optional; defaults from spec
  client.authentications['ApiKeyAuth'].apiKey = 'your-api-key';

  const queries = new QueriesApi();
  const body = new NLQueryRequest();
  body.query = 'CO2 emissions for France';

  const res = await queries.queryNlPost(body);
  console.log(res);
})();
