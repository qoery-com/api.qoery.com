// Natural Language Query via SDK (GET)
const Qoery = require('qoery');

const client = Qoery.ApiClient.instance;
const apiKeyAuth = client.authentications['ApiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR_API_KEY';

const queriesApi = new Qoery.QueriesApi();

const query = 'population of France';
const opts = {
  numResults: 10,
  paragraphExtraction: false,
  plot2table: 0
};

queriesApi.queryNlGet(query, opts, (error, data) => {
  if (error) {
    throw error;
  }
  console.log(data);
});