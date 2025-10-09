var Qoery = require('qoery');
var defaultClient = Qoery.ApiClient.instance;
defaultClient.authentications['ApiKeyAuth'].apiKey = "your-api-key";

var api = new Qoery.UsageApi();

api.usageGet({ uid: "00000000-0000-0000-0000-000000000000" }, function(err, data) {
  if (err) { console.error(err); return; }
  console.log(data.plan);
});
