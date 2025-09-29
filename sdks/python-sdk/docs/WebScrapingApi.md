# qoery.WebScrapingApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scrape_post**](WebScrapingApi.md#scrape_post) | **POST** /scrape | Structured Web Scrape


# **scrape_post**
> ScrapePost200Response scrape_post(html=html, markdown=markdown)

Structured Web Scrape

Download a web page, and structured data as time series. Use query params `html=true` and/or `markdown=true` to include raw artifacts inline; otherwise artifact URLs are provided in `artifacts`.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import qoery
from qoery.models.scrape_post200_response import ScrapePost200Response
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
    api_instance = qoery.WebScrapingApi(api_client)
    html = False # bool | Include page HTML inline in response (optional) (default to False)
    markdown = False # bool | Include page markdown inline in response (optional) (default to False)

    try:
        # Structured Web Scrape
        api_response = api_instance.scrape_post(html=html, markdown=markdown)
        print("The response of WebScrapingApi->scrape_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebScrapingApi->scrape_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **html** | **bool**| Include page HTML inline in response | [optional] [default to False]
 **markdown** | **bool**| Include page markdown inline in response | [optional] [default to False]

### Return type

[**ScrapePost200Response**](ScrapePost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  * X-RateLimit-Window - Time window in seconds <br>  * X-Concurrent-Limit - Maximum concurrent requests allowed <br>  * X-Concurrent-Current - Current number of concurrent requests <br>  |
**400** | Invalid URL or scraping failed |  -  |
**401** | Unauthorized |  -  |
**429** | Rate limit exceeded |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

