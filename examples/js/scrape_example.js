const { ApiClient, WebScrapingApi, URLRequest } = require('qoery');

(async () => {
  const client = ApiClient.instance;
  client.basePath = 'https://api.qoery.com/v0';
  client.authentications['ApiKeyAuth'].apiKey = 'your-api-key';

  const scraping = new WebScrapingApi();
  const body = new URLRequest();
  body.url = 'https://example.com';

  const res = await scraping.scrapePost(body);
  console.log(res);
})();
