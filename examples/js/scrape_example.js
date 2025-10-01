const response = await fetch("https://api.qoery.com/v0/scrape", {
  method: "POST",
  headers: {
    "X-API-Key": "your-api-key",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ url: "https://example.com/statistics" })
});

const data = await response.json();
console.log(`Cached: ${data.cached || false}`);
console.log(`Results: ${data.series.length} observations`);
