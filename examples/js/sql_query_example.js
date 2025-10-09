var Qoery = require('qoery');
var defaultClient = Qoery.ApiClient.instance;
defaultClient.authentications['ApiKeyAuth'].apiKey = "your-api-key";

var api = new Qoery.QueriesApi();
var req = new Qoery.QuerySqlPostRequest();
req.query = "SELECT * FROM series LIMIT 10";

api.querySqlPost(req, function(err, data) {
  if (err) { console.error(err); return; }
  console.log(data.sql_query);
});
