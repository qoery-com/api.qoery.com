var Qoery = require('qoery');
var defaultClient = Qoery.ApiClient.instance;
defaultClient.authentications['ApiKeyAuth'].apiKey = "your-api-key";

var api = new Qoery.WebScrapingApi();
var request = new Qoery.ScrapePostRequest();
request.url = "https://example.com/statistics";

api.scrapePost(request, function(err, data) {
  if (err) { console.error(err); return; }
  console.log(data.cached || false);
});
