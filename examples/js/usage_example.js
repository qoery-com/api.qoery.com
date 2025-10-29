// Usage for API key (GET)
async function run() {
  const url = new URL('https://api.qoery.com/v0/usage');
  url.searchParams.set('api_key', 'YOUR_API_KEY');

  const res = await fetch(url.toString(), {
    method: 'GET',
    headers: { 'X-API-Key': 'YOUR_API_KEY' }
  });
  const data = await res.json();
  console.log(data);
}

run().catch(console.error);
