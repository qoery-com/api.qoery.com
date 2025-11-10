# Qoery.DatasetsApi

All URIs are relative to *https://api.qoery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadDatasetCsv**](DatasetsApi.md#downloadDatasetCsv) | **GET** /v0/datasets/{job_id}/csv | Download the CSV file
[**getDatasetJobStatus**](DatasetsApi.md#getDatasetJobStatus) | **GET** /v0/datasets/{job_id} | Get job status and progress
[**listDatasetsOrStartJob**](DatasetsApi.md#listDatasetsOrStartJob) | **GET** /v0/datasets | List API endpoints or start a dataset collection job
[**startDatasetJob**](DatasetsApi.md#startDatasetJob) | **POST** /v0/datasets | Start a new dataset collection job



## downloadDatasetCsv

> File downloadDatasetCsv(jobId)

Download the CSV file

Downloads the CSV file containing the collected dataset. The file may be partial if the job is still processing.  **CSV Format:** - First row contains column headers - Each subsequent row represents a data point - Columns include: &#x60;url&#x60;, &#x60;title&#x60;, &#x60;value&#x60;, &#x60;dimension&#x60;, &#x60;timestamp&#x60; (if applicable) - Data is sorted by relevance score (most relevant first) - Partial CSVs are available while jobs are processing 

### Example

```javascript
import Qoery from 'qoery';
let defaultClient = Qoery.ApiClient.instance;
// Configure API key authorization: ApiKeyHeader
let ApiKeyHeader = defaultClient.authentications['ApiKeyHeader'];
ApiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeader.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';
// Configure Bearer (API_KEY) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Qoery.DatasetsApi();
let jobId = "20251110_151628"; // String | Unique identifier for the job
apiInstance.downloadDatasetCsv(jobId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobId** | **String**| Unique identifier for the job | 

### Return type

**File**

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/csv, application/json


## getDatasetJobStatus

> GetDatasetJobStatus200Response getDatasetJobStatus(jobId)

Get job status and progress

Returns the current status and progress of a dataset collection job. Poll this endpoint to check when the job completes.  **Status Values:** - &#x60;processing&#x60;: Job is actively collecting data - &#x60;completed&#x60;: Job finished successfully, CSV is ready - &#x60;error&#x60;: Job failed, check the &#x60;error&#x60; field for details  **Progress Steps:** - &#x60;initializing&#x60;: Setting up the job - &#x60;searching&#x60;: Finding relevant URLs - &#x60;scraping&#x60;: Extracting data from URLs - &#x60;processing&#x60;: Analyzing and structuring data - &#x60;finalizing&#x60;: Preparing the CSV output 

### Example

```javascript
import Qoery from 'qoery';
let defaultClient = Qoery.ApiClient.instance;
// Configure API key authorization: ApiKeyHeader
let ApiKeyHeader = defaultClient.authentications['ApiKeyHeader'];
ApiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeader.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';
// Configure Bearer (API_KEY) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Qoery.DatasetsApi();
let jobId = "20251110_151628"; // String | Unique identifier for the job
apiInstance.getDatasetJobStatus(jobId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobId** | **String**| Unique identifier for the job | 

### Return type

[**GetDatasetJobStatus200Response**](GetDatasetJobStatus200Response.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDatasetsOrStartJob

> ListDatasetsOrStartJob200Response listDatasetsOrStartJob(opts)

List API endpoints or start a dataset collection job

If no &#x60;search&#x60; query parameter is provided, returns API information. If &#x60;search&#x60; parameter is provided, starts a new dataset collection job.  **Job Lifecycle:** - Jobs start in &#x60;processing&#x60; status - Poll the job status endpoint to check progress - Jobs transition to &#x60;completed&#x60; when finished or &#x60;error&#x60; if they fail - Typical job duration: 1-5 minutes depending on query complexity - CSV files are available for download even while processing (partial data) 

### Example

```javascript
import Qoery from 'qoery';
let defaultClient = Qoery.ApiClient.instance;
// Configure API key authorization: ApiKeyHeader
let ApiKeyHeader = defaultClient.authentications['ApiKeyHeader'];
ApiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeader.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';
// Configure Bearer (API_KEY) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Qoery.DatasetsApi();
let opts = {
  'search': "search_example" // String | Search query to start a dataset collection job
};
apiInstance.listDatasetsOrStartJob(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **String**| Search query to start a dataset collection job | [optional] 

### Return type

[**ListDatasetsOrStartJob200Response**](ListDatasetsOrStartJob200Response.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startDatasetJob

> ListDatasetsOrStartJob200ResponseOneOf1 startDatasetJob(opts)

Start a new dataset collection job

Starts a new dataset collection job with the provided search query. The job runs asynchronously in the background.  **Job Lifecycle:** - Jobs start in &#x60;processing&#x60; status - Poll the job status endpoint to check progress - Jobs transition to &#x60;completed&#x60; when finished or &#x60;error&#x60; if they fail - Typical job duration: 1-5 minutes depending on query complexity - CSV files are available for download even while processing (partial data) 

### Example

```javascript
import Qoery from 'qoery';
let defaultClient = Qoery.ApiClient.instance;
// Configure API key authorization: ApiKeyHeader
let ApiKeyHeader = defaultClient.authentications['ApiKeyHeader'];
ApiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeader.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';
// Configure Bearer (API_KEY) access token for authorization: BearerAuth
let BearerAuth = defaultClient.authentications['BearerAuth'];
BearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Qoery.DatasetsApi();
let opts = {
  'search': "search_example", // String | Search query (alternative to request body)
  'startDatasetJobRequest': {"search":"climate change statistics"} // StartDatasetJobRequest | Request body with search query. Alternatively, you can provide `search` as a query parameter. 
};
apiInstance.startDatasetJob(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **String**| Search query (alternative to request body) | [optional] 
 **startDatasetJobRequest** | [**StartDatasetJobRequest**](StartDatasetJobRequest.md)| Request body with search query. Alternatively, you can provide &#x60;search&#x60; as a query parameter.  | [optional] 

### Return type

[**ListDatasetsOrStartJob200ResponseOneOf1**](ListDatasetsOrStartJob200ResponseOneOf1.md)

### Authorization

[ApiKeyHeader](../README.md#ApiKeyHeader), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

