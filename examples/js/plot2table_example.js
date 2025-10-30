// Example: Convert chart image to data table via SDK (GET)
const Qoery = require('qoery');

const client = Qoery.ApiClient.instance;
const apiKeyAuth = client.authentications['ApiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR_API_KEY';

const scrapingApi = new Qoery.WebScrapingApi();

const opts = { imageUrl: 'https://example.com/chart.png' };

scrapingApi.plot2tableGet(opts, (error, data) => {
  if (error) {
    throw error;
  }
  console.log(data);
});
