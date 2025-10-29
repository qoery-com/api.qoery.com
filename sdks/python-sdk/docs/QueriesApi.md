# qoery.QueriesApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_nl_get**](QueriesApi.md#query_nl_get) | **GET** /query/nl | Natural Language Query


# **query_nl_get**
> QueryNlGet200Response query_nl_get(query, num_results=num_results, paragraph_extraction=paragraph_extraction, plot2table=plot2table)

Natural Language Query

We search the public web for the most relevant sources to your query, extract structured data, and return curated series.

How it works:
- We query the web and fetch the top `num_results` relevant pages.
- We always extract tabular/JSON-like data when available.
- If `paragraph_extraction` is true, we scan prose paragraphs to identify statistics and convert them into series (e.g., "In 2000, there were 5,000 Swedes in Norway; in 2020, 50,000" → year/value pairs).
- If `plot2table` > 0, we analyze images of plots and extract their underlying datapoints.

Credits:
- Base credits = ceil(num_results / 10), minimum 1.
- Paragraph extraction surcharge = +1 credit when `paragraph_extraction` is true.
- Plot2Table credits = 1 per chart processed when `plot2table` > 0.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import qoery
from qoery.models.query_nl_get200_response import QueryNlGet200Response
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
    api_instance = qoery.QueriesApi(api_client)
    query = 'query_example' # str | Natural language query
    num_results = 10 # int | Number of top relevant pages to fetch and process (optional) (default to 10)
    paragraph_extraction = False # bool | Extract statistics from paragraph text and convert to structured series (year/value pairs) (optional) (default to False)
    plot2table = 0 # int | Number of plot images to analyze and convert into raw datapoints (optional) (default to 0)

    try:
        # Natural Language Query
        api_response = api_instance.query_nl_get(query, num_results=num_results, paragraph_extraction=paragraph_extraction, plot2table=plot2table)
        print("The response of QueriesApi->query_nl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueriesApi->query_nl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Natural language query | 
 **num_results** | **int**| Number of top relevant pages to fetch and process | [optional] [default to 10]
 **paragraph_extraction** | **bool**| Extract statistics from paragraph text and convert to structured series (year/value pairs) | [optional] [default to False]
 **plot2table** | **int**| Number of plot images to analyze and convert into raw datapoints | [optional] [default to 0]

### Return type

[**QueryNlGet200Response**](QueryNlGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  * X-RateLimit-Window - Time window in seconds <br>  * X-Concurrent-Limit - Maximum concurrent requests allowed <br>  * X-Concurrent-Current - Current number of concurrent requests <br>  |
**400** | Invalid input |  -  |
**401** | Unauthorized |  -  |
**429** | Rate limit exceeded |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  * X-RateLimit-Window - Time window in seconds <br>  * X-Concurrent-Limit - Maximum concurrent requests allowed <br>  * X-Concurrent-Current - Current number of concurrent requests <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

