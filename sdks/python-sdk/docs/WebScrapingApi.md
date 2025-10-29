# qoery.WebScrapingApi

All URIs are relative to *https://api.qoery.com/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plot2table_get**](WebScrapingApi.md#plot2table_get) | **GET** /plot2table | Convert Charts to Data Tables
[**scrape_get**](WebScrapingApi.md#scrape_get) | **GET** /scrape | Structured Web Scrape


# **plot2table_get**
> QueryNlGet200Response plot2table_get(image_url)

Convert Charts to Data Tables

Provide an image URL of a plot or chart and receive the underlying datapoints as structured series.
Supports time series, categorical, and scatter charts.

Credits: 1 Plot2Table credit per image processed.


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
**200** | Successfully converted chart to structured data points |  -  |
**400** | Bad request - missing or invalid parameters |  -  |
**401** | Unauthorized |  -  |
**429** | Rate limit exceeded |  * X-RateLimit-Limit - Maximum requests allowed per time window <br>  * X-RateLimit-Remaining - Number of requests remaining in current window <br>  * X-RateLimit-Reset - Unix timestamp when the rate limit resets <br>  * X-RateLimit-Window - Time window in seconds <br>  * X-Concurrent-Limit - Maximum concurrent requests allowed <br>  * X-Concurrent-Current - Current number of concurrent requests <br>  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scrape_get**
> ScrapeGet200Response scrape_get(url, query=query, paragraph_extraction=paragraph_extraction, plot2table=plot2table)

Structured Web Scrape

We search the public web for the most relevant sources to your query, extract structured data, and return curated series.

How it works:
- We always extract tabular/JSON-like data when available.
- If `paragraph_extraction` is true, we scan prose paragraphs to identify statistics and convert them into series (e.g., "In 2000, there were 5,000 Swedes in Norway; in 2020, 50,000" → year/value pairs).
- If `plot2table` > 0, we analyze images of plots and extract their underlying datapoints.

Credits:
- 1 Scrape credit per request.
- Paragraph extraction surcharge = +1 credit when `paragraph_extraction` is true.
- Plot2Table credits = 1 per chart processed when `plot2table` > 0.


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
    query = 'query_example' # str | Optional hint to guide extraction focus for this URL (optional)
    paragraph_extraction = False # bool | Extract statistics from paragraphs and convert to structured series (optional) (default to False)
    plot2table = 0 # int | Number of plot images to analyze and convert into raw datapoints (optional) (default to 0)

    try:
        # Structured Web Scrape
        api_response = api_instance.scrape_get(url, query=query, paragraph_extraction=paragraph_extraction, plot2table=plot2table)
        print("The response of WebScrapingApi->scrape_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebScrapingApi->scrape_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL to scrape | 
 **query** | **str**| Optional hint to guide extraction focus for this URL | [optional] 
 **paragraph_extraction** | **bool**| Extract statistics from paragraphs and convert to structured series | [optional] [default to False]
 **plot2table** | **int**| Number of plot images to analyze and convert into raw datapoints | [optional] [default to 0]

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

