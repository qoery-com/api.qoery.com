# Qoery.WebScrapingApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plot2tableGet**](WebScrapingApi.md#plot2tableGet) | **GET** /plot2table | Convert Charts to Data Tables
[**scrapeGet**](WebScrapingApi.md#scrapeGet) | **GET** /scrape | Structured Web Scrape



## plot2tableGet

> QueryNlGet200Response plot2tableGet(imageUrl)

Convert Charts to Data Tables

Convert charts, graphs, and other visual data representations into structured data points using AI. Supports time series, categorical, scatter plots, and other chart types.

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

Download a web page, and structured data as time series. Use query parameters to specify options.

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
  'query': "query_example", // String | Optional user query to guide extraction
  'enableScreenshots': false, // Boolean | Enable screenshot capture during scraping
  'html': false, // Boolean | Include page HTML inline in response
  'markdown': false // Boolean | Include page markdown inline in response
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
 **query** | **String**| Optional user query to guide extraction | [optional] 
 **enableScreenshots** | **Boolean**| Enable screenshot capture during scraping | [optional] [default to false]
 **html** | **Boolean**| Include page HTML inline in response | [optional] [default to false]
 **markdown** | **Boolean**| Include page markdown inline in response | [optional] [default to false]

### Return type

[**ScrapeGet200Response**](ScrapeGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

