const { ApiClient, QueriesApi, SQLQueryRequest } = require('qoery');

(async () => {
  const client = ApiClient.instance;
  client.basePath = 'https://api.qoery.com/v0';
  client.authentications['ApiKeyAuth'].apiKey = 'your-api-key';

  const queries = new QueriesApi();
  const body = new SQLQueryRequest();
  body.sql = 'SELECT * FROM emissions';

  const res = await queries.querySqlPost(body);
  console.log(res);
})();
