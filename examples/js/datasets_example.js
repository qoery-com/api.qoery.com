const Qoery = require('qoery');

const client = Qoery.ApiClient.instance;
client.authentications['ApiKeyAuth'].apiKey = 'YOUR_API_KEY';

const api = new Qoery.DatasetsApi();

// Start job
api.startDatasetJob({ search: 'climate change' }, (error, job) => {
  if (error) throw error;
  console.log(`Job ID: ${job.job_id}`);
  
  // Get status
  api.getDatasetJobStatus(job.job_id, (error, status) => {
    if (error) throw error;
    console.log(`Status: ${status.status}`);
    
    // Download CSV
    api.downloadDatasetCsv(job.job_id, (error, csv) => {
      if (error) throw error;
      console.log(`CSV: ${csv.size || csv.length} bytes`);
    });
  });
});
