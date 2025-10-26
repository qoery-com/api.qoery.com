// Example: Convert chart image to data table
const response = await fetch('https://api.qoery.com/v0/plot2table?image_url=https://example.com/chart.png', {
  method: 'GET',
  headers: {
    'X-API-Key': 'YOUR_API_KEY'
  }
});

const data = await response.json();
console.log(data);
