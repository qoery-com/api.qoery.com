const { ApiClient, QueriesApi, SQLQueryRequest } = require('qoery');

(async () => {
  const client = ApiClient.instance;
  client.basePath = 'https://api.qoery.com/v0';
  client.authentications['ApiKeyAuth'].apiKey = 'your-api-key';

  const queries = new QueriesApi();
  const body = new SQLQueryRequest();
  // Use 'query' field (sql_query also supported for backward compatibility)
  body.query = "SELECT date, value FROM emissions WHERE country = 'France' LIMIT 10";

  const res = await queries.querySqlPost(body);
  
  // Response includes: series, sql_query, metadata
  console.log('Executed SQL:', res.sql_query);
  console.log('Series count:', res.series.length);
  res.series.forEach(s => {
    console.log(`  ${s.name}: ${s.observations.length} observations`);
  });
})();
