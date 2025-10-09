const response = await fetch("https://api.qoery.com/v0/usage?uid=00000000-0000-0000-0000-000000000000", {
  headers: { "X-API-Key": "your-api-key" }
});

if (!response.ok) {
  const errText = await response.text();
  throw new Error(`Request failed: ${response.status} ${errText}`);
}

const data = await response.json();
console.log(`Plan: ${data.plan}`);
console.log(`Period: ${data.period_start} -> ${data.period_end}`);
console.log(`NL calls: ${data.endpoints.nl.calls_used}/${data.endpoints.nl.calls_limit} (remaining: ${data.endpoints.nl.remaining})`);
console.log(`SQL calls: ${data.endpoints.sql.calls_used}/${data.endpoints.sql.calls_limit} (remaining: ${data.endpoints.sql.remaining})`);
console.log(`Scrape calls: ${data.endpoints.scrape.calls_used}/${data.endpoints.scrape.calls_limit} (remaining: ${data.endpoints.scrape.remaining})`);
