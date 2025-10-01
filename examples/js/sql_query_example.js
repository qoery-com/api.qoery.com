const response = await fetch("https://api.qoery.com/v0/query/sql", {
  method: "POST",
  headers: {
    "X-API-Key": "your-api-key",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ query: "SELECT * FROM series LIMIT 10" })
});

const data = await response.json();
console.log(`Results: ${data.series.length} observations`);
