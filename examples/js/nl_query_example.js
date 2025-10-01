const response = await fetch("https://api.qoery.com/v0/query/nl", {
  method: "POST",
  headers: {
    "X-API-Key": "your-api-key",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ query: "population of France" })
});

const data = await response.json();
console.log(`Generated SQL: ${data.sql_query}`);
console.log(`Results: ${data.series.length} observations`);
