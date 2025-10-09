const response = await fetch("https://api.qoery.com/v0/query/sql", {
  method: "POST",
  headers: {
    "X-API-Key": "your-api-key",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ query: "SELECT * FROM series LIMIT 10" })
});

if (!response.ok) {
  const errText = await response.text();
  throw new Error(`Request failed: ${response.status} ${errText}`);
}

const data = await response.json();
console.log(`Executed SQL: ${data.sql_query}`);
console.log(`Series returned: ${data.series.length}`);
console.log(`Total results (meta.result_count): ${data.meta.result_count}`);
