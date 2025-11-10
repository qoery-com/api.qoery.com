# Qoery.HealthApi

All URIs are relative to *https://api.qoery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthCheck**](HealthApi.md#healthCheck) | **GET** /health | Health Check
[**rootStatus**](HealthApi.md#rootStatus) | **GET** / | Root Status



## healthCheck

> HealthResponse healthCheck()

Health Check

Check the health status of the API

### Example

```javascript
import Qoery from 'qoery';

let apiInstance = new Qoery.HealthApi();
apiInstance.healthCheck((error, data, response) => {
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

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rootStatus

> RootStatus200Response rootStatus()

Root Status

Root endpoint for health checks

### Example

```javascript
import Qoery from 'qoery';

let apiInstance = new Qoery.HealthApi();
apiInstance.rootStatus((error, data, response) => {
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

[**RootStatus200Response**](RootStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

