const Qoery = require('qoery');

const client = Qoery.ApiClient.instance;
client.authentications['ApiKeyAuth'].apiKey = 'YOUR_API_KEY';

const api = new Qoery.PlansApi();

api.listPlans((error, plans) => {
  if (error) throw error;
  console.log(`Plans: ${Object.keys(plans.plans).join(', ')}`);
});
