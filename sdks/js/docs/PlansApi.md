# Qoery.PlansApi

All URIs are relative to *https://api.qoery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listPlans**](PlansApi.md#listPlans) | **GET** /v0/plans | List subscription plans and endpoint limits



## listPlans

> ListPlans200Response listPlans()

List subscription plans and endpoint limits

Returns all available subscription plans with pricing metadata, monthly limits per endpoint, and other plan features.  **Plan Features:** - Each plan includes different monthly quotas per endpoint - Limits reset on the 1st of each month - Plans can be upgraded/downgraded at any time - Annual billing offers discounts compared to monthly billing 

### Example

```javascript
import Qoery from 'qoery';

let apiInstance = new Qoery.PlansApi();
apiInstance.listPlans((error, data, response) => {
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

[**ListPlans200Response**](ListPlans200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

