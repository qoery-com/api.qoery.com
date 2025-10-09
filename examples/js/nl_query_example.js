const response = await fetch("https://api.qoery.com/v0/query/nl", {
  method: "POST",
  headers: {
    "X-API-Key": "your-api-key",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ query: "population of France" })
});

if (!response.ok) {
  const errText = await response.text();
  throw new Error(`Request failed: ${response.status} ${errText}`);
}

const data = await response.json();
console.log(`Generated SQL: ${data.sql_query}`);
console.log(`Series returned: ${data.series.length}`);
console.log(`Total results (meta.result_count): ${data.meta.result_count}`);
if (data.description) {
  console.log(`Description: ${data.description}`);
}
