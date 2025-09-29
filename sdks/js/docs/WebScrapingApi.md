# Qoery.WebScrapingApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scrapePost**](WebScrapingApi.md#scrapePost) | **POST** /scrape | Structured Web Scrape



## scrapePost

> ScrapePost200Response scrapePost(opts)

Structured Web Scrape

Download a web page, and structured data as time series. Use query params &#x60;html&#x3D;true&#x60; and/or &#x60;markdown&#x3D;true&#x60; to include raw artifacts inline; otherwise artifact URLs are provided in &#x60;artifacts&#x60;.

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
let opts = {
  'html': false, // Boolean | Include page HTML inline in response
  'markdown': false // Boolean | Include page markdown inline in response
};
apiInstance.scrapePost(opts, (error, data, response) => {
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
 **html** | **Boolean**| Include page HTML inline in response | [optional] [default to false]
 **markdown** | **Boolean**| Include page markdown inline in response | [optional] [default to false]

### Return type

[**ScrapePost200Response**](ScrapePost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

