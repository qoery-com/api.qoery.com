// Natural Language Query (GET)
async function run() {
  const url = new URL('https://api.qoery.com/v0/query/nl');
  url.searchParams.set('query', 'population of France');
  url.searchParams.set('num_results', '10');
  url.searchParams.set('paragraph_extraction', 'false');
  url.searchParams.set('plot2table', '0');

  const res = await fetch(url.toString(), {
    method: 'GET',
    headers: { 'X-API-Key': 'YOUR_API_KEY' }
  });
  const data = await res.json();
  console.log(data);
}

run().catch(console.error);