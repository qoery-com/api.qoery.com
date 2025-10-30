// Structured Web Scrape via SDK (GET)
const Qoery = require('qoery');

const client = Qoery.ApiClient.instance;
const apiKeyAuth = client.authentications['ApiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR_API_KEY';

const scrapingApi = new Qoery.WebScrapingApi();

const opts = {
  url: 'https://example.com/statistics',
  paragraphExtraction: false,
  plot2table: 0
};

scrapingApi.scrapeGet(opts, (error, data) => {
  if (error) {
    throw error;
  }
  console.log(data);
});
