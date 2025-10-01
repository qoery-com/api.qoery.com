const response = await fetch("https://api.qoery.com/v0/usage?uid=your-user-id", {
  headers: { "X-API-Key": "your-api-key" }
});

const data = await response.json();
console.log(`Plan: ${data.plan}`);
console.log(`NL calls: ${data.endpoints.nl.calls_used}/${data.endpoints.nl.calls_limit}`);
console.log(`SQL calls: ${data.endpoints.sql.calls_used}/${data.endpoints.sql.calls_limit}`);
console.log(`Scrape calls: ${data.endpoints.scrape.calls_used}/${data.endpoints.scrape.calls_limit}`);
