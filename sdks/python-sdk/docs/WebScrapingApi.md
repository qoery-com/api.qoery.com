# qoery.WebScrapingApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plot2table_get**](WebScrapingApi.md#plot2table_get) | **GET** /plot2table | Convert Charts to Data Tables
[**scrape_get**](WebScrapingApi.md#scrape_get) | **GET** /scrape | Structured Web Scrape


# **plot2table_get**
> QueryNlGet200Response plot2table_get(image_url)

Convert Charts to Data Tables

Convert charts, graphs, and other visual data representations into structured data tables using AI.

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
    api_instance = qoery.WebScrapingApi(api_client)
    image_url = 'image_url_example' # str | URL of the image containing charts or graphs to convert to data table

    try:
        # Convert Charts to Data Tables
        api_response = api_instance.plot2table_get(image_url)
        print("The response of WebScrapingApi->plot2table_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebScrapingApi->plot2table_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_url** | **str**| URL of the image containing charts or graphs to convert to data table | 

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
**200** | Successfully converted chart to data table |  -  |
**400** | Bad request - missing or invalid parameters |  -  |
**401** | Unauthorized |  -  |
**429** | Rate limit exceeded |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  * X-RateLimit-Window - Time window in seconds <br>  * X-Concurrent-Limit - Maximum concurrent requests allowed <br>  * X-Concurrent-Current - Current number of concurrent requests <br>  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scrape_get**
> ScrapeGet200Response scrape_get(url, query=query, enable_screenshots=enable_screenshots, html=html, markdown=markdown)

Structured Web Scrape

Download a web page, and structured data as time series. Use query parameters to specify options.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import qoery
from qoery.models.scrape_get200_response import ScrapeGet200Response
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
    url = 'url_example' # str | URL to scrape
    query = 'query_example' # str | Optional user query to guide extraction (optional)
    enable_screenshots = False # bool | Enable screenshot capture during scraping (optional) (default to False)
    html = False # bool | Include page HTML inline in response (optional) (default to False)
    markdown = False # bool | Include page markdown inline in response (optional) (default to False)

    try:
        # Structured Web Scrape
        api_response = api_instance.scrape_get(url, query=query, enable_screenshots=enable_screenshots, html=html, markdown=markdown)
        print("The response of WebScrapingApi->scrape_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebScrapingApi->scrape_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL to scrape | 
 **query** | **str**| Optional user query to guide extraction | [optional] 
 **enable_screenshots** | **bool**| Enable screenshot capture during scraping | [optional] [default to False]
 **html** | **bool**| Include page HTML inline in response | [optional] [default to False]
 **markdown** | **bool**| Include page markdown inline in response | [optional] [default to False]

### Return type

[**ScrapeGet200Response**](ScrapeGet200Response.md)

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
**429** | Rate limit exceeded |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  * X-RateLimit-Window - Time window in seconds <br>  * X-Concurrent-Limit - Maximum concurrent requests allowed <br>  * X-Concurrent-Current - Current number of concurrent requests <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

