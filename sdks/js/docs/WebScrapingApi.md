# Qoery.WebScrapingApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plot2tableGet**](WebScrapingApi.md#plot2tableGet) | **GET** /plot2table | Convert Charts to Data Tables
[**scrapeGet**](WebScrapingApi.md#scrapeGet) | **GET** /scrape | Structured Web Scrape



## plot2tableGet

> QueryNlGet200Response plot2tableGet(imageUrl)

Convert Charts to Data Tables

Provide an image URL of a plot or chart and receive the underlying datapoints as structured series. Supports time series, categorical, and scatter charts.  Credits: 1 Plot2Table credit per image processed. 

### Example

```javascript
import Qoery from 'qoery';
let defaultClient = Qoery.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Qoery.WebScrapingApi();
let imageUrl = "imageUrl_example"; // String | URL of the image containing charts or graphs to convert to data table
apiInstance.plot2tableGet(imageUrl, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageUrl** | **String**| URL of the image containing charts or graphs to convert to data table | 

### Return type

[**QueryNlGet200Response**](QueryNlGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scrapeGet

> ScrapeGet200Response scrapeGet(url, opts)

Structured Web Scrape

We search the public web for the most relevant sources to your query, extract structured data, and return curated series.  How it works: - We always extract tabular/JSON-like data when available. - If &#x60;paragraph_extraction&#x60; is true, we scan prose paragraphs to identify statistics and convert them into series (e.g., \&quot;In 2000, there were 5,000 Swedes in Norway; in 2020, 50,000\&quot; → year/value pairs). - If &#x60;plot2table&#x60; &gt; 0, we analyze images of plots and extract their underlying datapoints.  Credits: - 1 Scrape credit per request. - Paragraph extraction surcharge &#x3D; +1 credit when &#x60;paragraph_extraction&#x60; is true. - Plot2Table credits &#x3D; 1 per chart processed when &#x60;plot2table&#x60; &gt; 0. 

### Example

```javascript
import Qoery from 'qoery';
let defaultClient = Qoery.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Qoery.WebScrapingApi();
let url = "url_example"; // String | URL to scrape
let opts = {
  'query': "query_example", // String | Optional hint to guide extraction focus for this URL
  'paragraphExtraction': false, // Boolean | Extract statistics from paragraphs and convert to structured series
  'plot2table': 0 // Number | Number of plot images to analyze and convert into raw datapoints
};
apiInstance.scrapeGet(url, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **String**| URL to scrape | 
 **query** | **String**| Optional hint to guide extraction focus for this URL | [optional] 
 **paragraphExtraction** | **Boolean**| Extract statistics from paragraphs and convert to structured series | [optional] [default to false]
 **plot2table** | **Number**| Number of plot images to analyze and convert into raw datapoints | [optional] [default to 0]

### Return type

[**ScrapeGet200Response**](ScrapeGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

