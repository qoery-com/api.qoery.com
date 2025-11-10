# qoery.HealthApi

All URIs are relative to *https://api.qoery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](HealthApi.md#health_check) | **GET** /health | Health Check
[**root_status**](HealthApi.md#root_status) | **GET** / | Root Status


# **health_check**
> HealthResponse health_check()

Health Check

Check the health status of the API

### Example


```python
import qoery
from qoery.models.health_response import HealthResponse
from qoery.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qoery.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qoery.Configuration(
    host = "https://api.qoery.com"
)


# Enter a context with an instance of the API client
with qoery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qoery.HealthApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check()
        print("The response of HealthApi->health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->health_check: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is healthy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_status**
> RootStatus200Response root_status()

Root Status

Root endpoint for health checks

### Example


```python
import qoery
from qoery.models.root_status200_response import RootStatus200Response
from qoery.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qoery.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qoery.Configuration(
    host = "https://api.qoery.com"
)


# Enter a context with an instance of the API client
with qoery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qoery.HealthApi(api_client)

    try:
        # Root Status
        api_response = api_instance.root_status()
        print("The response of HealthApi->root_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->root_status: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is running |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

