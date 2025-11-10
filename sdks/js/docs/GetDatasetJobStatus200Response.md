# Qoery.GetDatasetJobStatus200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobId** | **String** | Unique identifier for the job | 
**status** | **String** | Current job status. Possible values: - &#x60;processing&#x60;: Job is actively collecting and processing data - &#x60;completed&#x60;: Job finished successfully, CSV is ready for download - &#x60;error&#x60;: Job failed, check the &#x60;error&#x60; field for details  | 
**query** | **String** | Original search query | 
**progress** | [**GetDatasetJobStatus200ResponseProgress**](GetDatasetJobStatus200ResponseProgress.md) |  | 
**urls** | **[String]** | List of URLs being processed | 
**csvUrl** | **String** | URL to download the CSV file | 
**error** | **String** | Error message if status is &#39;error&#39; | 
**startedAt** | **Date** | Timestamp when the job started | 
**completedAt** | **Date** | Timestamp when the job completed (null if still processing) | 



## Enum: StatusEnum


* `processing` (value: `"processing"`)

* `completed` (value: `"completed"`)

* `error` (value: `"error"`)




