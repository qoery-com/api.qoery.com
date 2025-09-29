# QoerysApi.UsageApi

All URIs are relative to *https://api.qoery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usageGet**](UsageApi.md#usageGet) | **GET** /usage | Get usage statistics



## usageGet

> UsageGet200Response usageGet()

Get usage statistics

Get current usage and rate limit information

### Example

```javascript
import QoerysApi from 'qoerys_api';
let defaultClient = QoerysApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new QoerysApi.UsageApi();
apiInstance.usageGet((error, data, response) => {
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

[**UsageGet200Response**](UsageGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

