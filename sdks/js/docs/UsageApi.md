# Qoery.UsageApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plansGet**](UsageApi.md#plansGet) | **GET** /plans | List subscription plans and endpoint limits
[**usageGet**](UsageApi.md#usageGet) | **GET** /usage | Get usage statistics



## plansGet

> PlansGet200Response plansGet()

List subscription plans and endpoint limits

Returns available plans with pricing metadata and monthly limits per endpoint.

### Example

```javascript
import Qoery from 'qoery';
let defaultClient = Qoery.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Qoery.UsageApi();
apiInstance.plansGet((error, data, response) => {
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

[**PlansGet200Response**](PlansGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usageGet

> UsageGet200Response usageGet(apiKey)

Get usage statistics

Get current usage and rate limit information per endpoint for the provided API key

### Example

```javascript
import Qoery from 'qoery';
let defaultClient = Qoery.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Qoery.UsageApi();
let apiKey = "apiKey_example"; // String | API key to look up usage for
apiInstance.usageGet(apiKey, (error, data, response) => {
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
 **apiKey** | **String**| API key to look up usage for | 

### Return type

[**UsageGet200Response**](UsageGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

