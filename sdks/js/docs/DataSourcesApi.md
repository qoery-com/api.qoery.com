# QoerysApi.DataSourcesApi

All URIs are relative to *https://api.qoery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scrapePost**](DataSourcesApi.md#scrapePost) | **POST** /scrape | Scrape URL → return series



## scrapePost

> [QueryNlPost200ResponseSeriesInner] scrapePost()

Scrape URL → return series

### Example

```javascript
import QoerysApi from 'qoerys_api';
let defaultClient = QoerysApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new QoerysApi.DataSourcesApi();
apiInstance.scrapePost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[QueryNlPost200ResponseSeriesInner]**](QueryNlPost200ResponseSeriesInner.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

