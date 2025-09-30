const { ApiClient, WebScrapingApi, URLRequest } = require('qoery');

(async () => {
  const client = ApiClient.instance;
  client.basePath = 'https://api.qoery.com/v0';
  client.authentications['ApiKeyAuth'].apiKey = 'your-api-key';

  const scraping = new WebScrapingApi();
  const body = new URLRequest();
  body.url = 'https://example.com/statistics';

  // Use markdown=true and/or html=true query params to include content inline
  const res = await scraping.scrapePost(body, { markdown: true });
  
  // Response includes: series, artifacts, cached (if from cache), source_id
  console.log('Cached:', res.cached || false);
  console.log('Series count:', res.series.length);
  if (res.markdown) {
    console.log('Markdown length:', res.markdown.length, 'chars');
  }
})();
