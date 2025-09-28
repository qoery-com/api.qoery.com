# openapi_client.QueriesApi

All URIs are relative to *https://api.qoery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_nl_post**](QueriesApi.md#query_nl_post) | **POST** /query/nl | Natural language → SQL → time series
[**query_sql_post**](QueriesApi.md#query_sql_post) | **POST** /query/sql | Execute SQL → return time series


# **query_nl_post**
> QueryNlPost200Response query_nl_post(query_nl_post_request)

Natural language → SQL → time series

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.query_nl_post200_response import QueryNlPost200Response
from openapi_client.models.query_nl_post_request import QueryNlPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qoery.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.qoery.com"
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.QueriesApi(api_client)
    query_nl_post_request = openapi_client.QueryNlPostRequest() # QueryNlPostRequest | 

    try:
        # Natural language → SQL → time series
        api_response = api_instance.query_nl_post(query_nl_post_request)
        print("The response of QueriesApi->query_nl_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueriesApi->query_nl_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_nl_post_request** | [**QueryNlPostRequest**](QueryNlPostRequest.md)|  | 

### Return type

[**QueryNlPost200Response**](QueryNlPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  * X-RateLimit-Window - Time window in seconds <br>  * X-Concurrent-Limit - Maximum concurrent requests allowed <br>  * X-Concurrent-Current - Current number of concurrent requests <br>  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**429** | Rate limit exceeded |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_sql_post**
> QueryNlPost200Response query_sql_post(query_sql_post_request)

Execute SQL → return time series

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.query_nl_post200_response import QueryNlPost200Response
from openapi_client.models.query_sql_post_request import QuerySqlPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qoery.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.qoery.com"
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.QueriesApi(api_client)
    query_sql_post_request = openapi_client.QuerySqlPostRequest() # QuerySqlPostRequest | 

    try:
        # Execute SQL → return time series
        api_response = api_instance.query_sql_post(query_sql_post_request)
        print("The response of QueriesApi->query_sql_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueriesApi->query_sql_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_sql_post_request** | [**QuerySqlPostRequest**](QuerySqlPostRequest.md)|  | 

### Return type

[**QueryNlPost200Response**](QueryNlPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  * X-RateLimit-Window - Time window in seconds <br>  * X-Concurrent-Limit - Maximum concurrent requests allowed <br>  * X-Concurrent-Current - Current number of concurrent requests <br>  |
**400** | Invalid SQL or mapping failure |  -  |
**401** | Unauthorized |  -  |
**429** | Rate limit exceeded |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

