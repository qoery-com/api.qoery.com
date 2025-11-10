const Qoery = require('qoery');

const client = Qoery.ApiClient.instance;
client.authentications['ApiKeyAuth'].apiKey = 'YOUR_API_KEY';

const api = new Qoery.DatasetsApi();

// Start job
const request = new Qoery.V0DatasetsPostRequest();
request.search = 'climate change';

api.v0DatasetsPost(request, (error, job) => {
  if (error) throw error;
  console.log(`Job ID: ${job.job_id}`);
  
  // Get status
  api.v0DatasetsJobIdGet(job.job_id, (error, status) => {
    if (error) throw error;
    console.log(`Status: ${status.status}`);
  });
});
