# qoery.UsageApi

All URIs are relative to *https://api.qoery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage_stats**](UsageApi.md#get_usage_stats) | **GET** /v0/usage | Get usage statistics


# **get_usage_stats**
> GetUsageStats200Response get_usage_stats(api_key=api_key, uid=uid, x_api_key=x_api_key, authorization=authorization)

Get usage statistics

Returns current usage statistics and quota information for the user.
Can be identified by either `api_key` or `uid` parameter.

**Usage Period:**
- Usage is tracked monthly, resetting on the 1st of each month
- Counts include all API calls, including errors
- Errors are tracked separately in the `errors` field


### Example


```python
import qoery
from qoery.models.get_usage_stats200_response import GetUsageStats200Response
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
    api_instance = qoery.UsageApi(api_client)
    api_key = 'api_key_example' # str | API key to look up usage for (alternative to uid) (optional)
    uid = 'uid_example' # str | User ID to look up usage for (alternative to api_key) (optional)
    x_api_key = 'x_api_key_example' # str | API key provided via header (optional)
    authorization = 'authorization_example' # str | API key provided as Bearer token (optional)

    try:
        # Get usage statistics
        api_response = api_instance.get_usage_stats(api_key=api_key, uid=uid, x_api_key=x_api_key, authorization=authorization)
        print("The response of UsageApi->get_usage_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_usage_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| API key to look up usage for (alternative to uid) | [optional] 
 **uid** | **str**| User ID to look up usage for (alternative to api_key) | [optional] 
 **x_api_key** | **str**| API key provided via header | [optional] 
 **authorization** | **str**| API key provided as Bearer token | [optional] 

### Return type

[**GetUsageStats200Response**](GetUsageStats200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage statistics |  * X-RateLimit-Limit - Monthly quota limit for this endpoint <br>  * X-RateLimit-Remaining - Remaining calls in current monthly period <br>  * X-RateLimit-Reset - Timestamp when the monthly quota resets <br>  |
**400** | Either uid or api_key is required |  -  |
**401** | Invalid API key |  -  |
**500** | Failed to fetch usage data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

