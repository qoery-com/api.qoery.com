# qoery.UsageApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plans_get**](UsageApi.md#plans_get) | **GET** /plans | List subscription plans and endpoint limits
[**usage_get**](UsageApi.md#usage_get) | **GET** /usage | Get usage statistics


# **plans_get**
> PlansGet200Response plans_get()

List subscription plans and endpoint limits

Returns available plans with pricing metadata and monthly limits per endpoint.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import qoery
from qoery.models.plans_get200_response import PlansGet200Response
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
    api_instance = qoery.UsageApi(api_client)

    try:
        # List subscription plans and endpoint limits
        api_response = api_instance.plans_get()
        print("The response of UsageApi->plans_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->plans_get: %s\n" % e)
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plans and limits |  -  |
**500** | Failed to load plans |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usage_get**
> UsageGet200Response usage_get(api_key)

Get usage statistics

Get current usage and rate limit information per endpoint for the provided API key

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import qoery
from qoery.models.usage_get200_response import UsageGet200Response
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
    api_instance = qoery.UsageApi(api_client)
    api_key = 'api_key_example' # str | API key to look up usage for

    try:
        # Get usage statistics
        api_response = api_instance.usage_get(api_key)
        print("The response of UsageApi->usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| API key to look up usage for | 

### Return type

[**UsageGet200Response**](UsageGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage statistics |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  * X-RateLimit-Window - Time window in seconds <br>  * X-Concurrent-Limit - Maximum concurrent requests allowed <br>  * X-Concurrent-Current - Current number of concurrent requests <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

