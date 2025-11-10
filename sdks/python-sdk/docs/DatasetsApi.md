# qoery.DatasetsApi

All URIs are relative to *https://api.qoery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_dataset_csv**](DatasetsApi.md#download_dataset_csv) | **GET** /v0/datasets/{job_id}/csv | Download the CSV file
[**get_dataset_job_status**](DatasetsApi.md#get_dataset_job_status) | **GET** /v0/datasets/{job_id} | Get job status and progress
[**list_datasets_or_start_job**](DatasetsApi.md#list_datasets_or_start_job) | **GET** /v0/datasets | List API endpoints or start a dataset collection job
[**start_dataset_job**](DatasetsApi.md#start_dataset_job) | **POST** /v0/datasets | Start a new dataset collection job


# **download_dataset_csv**
> bytearray download_dataset_csv(job_id)

Download the CSV file

Downloads the CSV file containing the collected dataset.
The file may be partial if the job is still processing.

**CSV Format:**
- First row contains column headers
- Each subsequent row represents a data point
- Columns include: `url`, `title`, `value`, `dimension`, `timestamp` (if applicable)
- Data is sorted by relevance score (most relevant first)
- Partial CSVs are available while jobs are processing


### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyAuth):
* Bearer (API_KEY) Authentication (BearerAuth):

```python
import qoery
from qoery.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qoery.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qoery.Configuration(
    host = "https://api.qoery.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeader
configuration.api_key['ApiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyHeader'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (API_KEY): BearerAuth
configuration = qoery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qoery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qoery.DatasetsApi(api_client)
    job_id = '20251110_151628' # str | Unique identifier for the job

    try:
        # Download the CSV file
        api_response = api_instance.download_dataset_csv(job_id)
        print("The response of DatasetsApi->download_dataset_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->download_dataset_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique identifier for the job | 

### Return type

**bytearray**

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV file download |  * Content-Disposition -  <br>  * Content-Type -  <br>  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | CSV not ready yet |  -  |
**429** | Rate limit exceeded - Monthly quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_job_status**
> GetDatasetJobStatus200Response get_dataset_job_status(job_id)

Get job status and progress

Returns the current status and progress of a dataset collection job.
Poll this endpoint to check when the job completes.

**Status Values:**
- `processing`: Job is actively collecting data
- `completed`: Job finished successfully, CSV is ready
- `error`: Job failed, check the `error` field for details

**Progress Steps:**
- `initializing`: Setting up the job
- `searching`: Finding relevant URLs
- `scraping`: Extracting data from URLs
- `processing`: Analyzing and structuring data
- `finalizing`: Preparing the CSV output


### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyAuth):
* Bearer (API_KEY) Authentication (BearerAuth):

```python
import qoery
from qoery.models.get_dataset_job_status200_response import GetDatasetJobStatus200Response
from qoery.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qoery.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qoery.Configuration(
    host = "https://api.qoery.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeader
configuration.api_key['ApiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyHeader'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (API_KEY): BearerAuth
configuration = qoery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qoery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qoery.DatasetsApi(api_client)
    job_id = '20251110_151628' # str | Unique identifier for the job

    try:
        # Get job status and progress
        api_response = api_instance.get_dataset_job_status(job_id)
        print("The response of DatasetsApi->get_dataset_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_dataset_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique identifier for the job | 

### Return type

[**GetDatasetJobStatus200Response**](GetDatasetJobStatus200Response.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job status and progress |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |
**429** | Rate limit exceeded - Monthly quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datasets_or_start_job**
> ListDatasetsOrStartJob200Response list_datasets_or_start_job(search=search)

List API endpoints or start a dataset collection job

If no `search` query parameter is provided, returns API information.
If `search` parameter is provided, starts a new dataset collection job.

**Job Lifecycle:**
- Jobs start in `processing` status
- Poll the job status endpoint to check progress
- Jobs transition to `completed` when finished or `error` if they fail
- Typical job duration: 1-5 minutes depending on query complexity
- CSV files are available for download even while processing (partial data)


### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyAuth):
* Bearer (API_KEY) Authentication (BearerAuth):

```python
import qoery
from qoery.models.list_datasets_or_start_job200_response import ListDatasetsOrStartJob200Response
from qoery.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qoery.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qoery.Configuration(
    host = "https://api.qoery.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeader
configuration.api_key['ApiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyHeader'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (API_KEY): BearerAuth
configuration = qoery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qoery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qoery.DatasetsApi(api_client)
    search = 'search_example' # str | Search query to start a dataset collection job (optional)

    try:
        # List API endpoints or start a dataset collection job
        api_response = api_instance.list_datasets_or_start_job(search=search)
        print("The response of DatasetsApi->list_datasets_or_start_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->list_datasets_or_start_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query to start a dataset collection job | [optional] 

### Return type

[**ListDatasetsOrStartJob200Response**](ListDatasetsOrStartJob200Response.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API information or job started |  -  |
**400** | Bad request - Invalid input parameters |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**429** | Rate limit exceeded - Monthly quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_dataset_job**
> ListDatasetsOrStartJob200ResponseOneOf1 start_dataset_job(search=search, start_dataset_job_request=start_dataset_job_request)

Start a new dataset collection job

Starts a new dataset collection job with the provided search query.
The job runs asynchronously in the background.

**Job Lifecycle:**
- Jobs start in `processing` status
- Poll the job status endpoint to check progress
- Jobs transition to `completed` when finished or `error` if they fail
- Typical job duration: 1-5 minutes depending on query complexity
- CSV files are available for download even while processing (partial data)


### Example

* Api Key Authentication (ApiKeyHeader):
* Api Key Authentication (ApiKeyAuth):
* Bearer (API_KEY) Authentication (BearerAuth):

```python
import qoery
from qoery.models.list_datasets_or_start_job200_response_one_of1 import ListDatasetsOrStartJob200ResponseOneOf1
from qoery.models.start_dataset_job_request import StartDatasetJobRequest
from qoery.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.qoery.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qoery.Configuration(
    host = "https://api.qoery.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyHeader
configuration.api_key['ApiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyHeader'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (API_KEY): BearerAuth
configuration = qoery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qoery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qoery.DatasetsApi(api_client)
    search = 'search_example' # str | Search query (alternative to request body) (optional)
    start_dataset_job_request = {"search":"climate change statistics"} # StartDatasetJobRequest | Request body with search query. Alternatively, you can provide `search` as a query parameter.  (optional)

    try:
        # Start a new dataset collection job
        api_response = api_instance.start_dataset_job(search=search, start_dataset_job_request=start_dataset_job_request)
        print("The response of DatasetsApi->start_dataset_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->start_dataset_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query (alternative to request body) | [optional] 
 **start_dataset_job_request** | [**StartDatasetJobRequest**](StartDatasetJobRequest.md)| Request body with search query. Alternatively, you can provide &#x60;search&#x60; as a query parameter.  | [optional] 

### Return type

[**ListDatasetsOrStartJob200ResponseOneOf1**](ListDatasetsOrStartJob200ResponseOneOf1.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job started successfully |  * X-RateLimit-Limit - Monthly quota limit for this endpoint <br>  * X-RateLimit-Remaining - Remaining calls in current monthly period <br>  * X-RateLimit-Reset - Timestamp when the monthly quota resets <br>  |
**400** | Bad request - Invalid input parameters |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**429** | Rate limit exceeded - Monthly quota exceeded |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

