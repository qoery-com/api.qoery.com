# qoery.SystemApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_get**](SystemApi.md#health_get) | **GET** /health | Health Check


# **health_get**
> HealthGet200Response health_get()

Health Check

Check the health status of the API

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import qoery
from qoery.models.health_get200_response import HealthGet200Response
from qoery.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qoery.com/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = qoery.Configuration(
    host = "https://api.qoery.com/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with qoery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qoery.SystemApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_get()
        print("The response of SystemApi->health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthGet200Response**](HealthGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is healthy |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

