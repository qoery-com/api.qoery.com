# Qoery.UsageApi

All URIs are relative to *https://api.qoery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUsageStats**](UsageApi.md#getUsageStats) | **GET** /v0/usage | Get usage statistics



## getUsageStats

> GetUsageStats200Response getUsageStats(opts)

Get usage statistics

Returns current usage statistics and quota information for the user. Can be identified by either &#x60;api_key&#x60; or &#x60;uid&#x60; parameter.  **Usage Period:** - Usage is tracked monthly, resetting on the 1st of each month - Counts include all API calls, including errors - Errors are tracked separately in the &#x60;errors&#x60; field 

### Example

```javascript
import Qoery from 'qoery';

let apiInstance = new Qoery.UsageApi();
let opts = {
  'apiKey': "apiKey_example", // String | API key to look up usage for (alternative to uid)
  'uid': "uid_example", // String | User ID to look up usage for (alternative to api_key)
  'xApiKey': "xApiKey_example", // String | API key provided via header
  'authorization': "authorization_example" // String | API key provided as Bearer token
};
apiInstance.getUsageStats(opts, (error, data, response) => {
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
 **apiKey** | **String**| API key to look up usage for (alternative to uid) | [optional] 
 **uid** | **String**| User ID to look up usage for (alternative to api_key) | [optional] 
 **xApiKey** | **String**| API key provided via header | [optional] 
 **authorization** | **String**| API key provided as Bearer token | [optional] 

### Return type

[**GetUsageStats200Response**](GetUsageStats200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

