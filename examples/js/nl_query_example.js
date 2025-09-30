const { ApiClient, QueriesApi, NLQueryRequest } = require('qoery');

(async () => {
  const client = ApiClient.instance;
  client.basePath = 'https://api.qoery.com/v0';
  client.authentications['ApiKeyAuth'].apiKey = 'your-api-key';

  const queries = new QueriesApi();
  const body = new NLQueryRequest();
  body.query = 'CO2 emissions for France from 2010 to 2020';

  const res = await queries.queryNlPost(body);
  
  // Response includes: sql_query, series, metadata, description
  console.log('Generated SQL:', res.sql_query);
  console.log('Series count:', res.series.length);
  res.series.forEach(s => {
    console.log(`  ${s.name}: ${s.observations.length} observations`);
  });
})();
