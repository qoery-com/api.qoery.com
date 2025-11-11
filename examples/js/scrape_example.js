// Structured Web Scrape via SDK (GET)
const Qoery = require('qoery');

const client = Qoery.ApiClient.instance;
const apiKeyAuth = client.authentications['ApiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR_API_KEY';

const scrapingApi = new Qoery.WebScrapingApi();

const url = 'https://example.com/statistics';
const opts = {
  paragraphExtraction: false,
  plot2table: 0
};

scrapingApi.scrapeGet(url, opts, (error, data) => {
  if (error) {
    throw error;
  }
  console.log(data);
});
