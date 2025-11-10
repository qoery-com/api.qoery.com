# Qoery.V0DatasetsJobIdGet200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobId** | **String** | Unique identifier for the job | 
**status** | **String** | Current job status | 
**query** | **String** | Original search query | 
**progress** | [**V0DatasetsJobIdGet200ResponseProgress**](V0DatasetsJobIdGet200ResponseProgress.md) |  | 
**urls** | **[String]** | List of URLs being processed | 
**csvUrl** | **String** | URL to download the CSV file | 
**error** | **String** | Error message if status is &#39;error&#39; | 
**startedAt** | **Date** | Timestamp when the job started | 
**completedAt** | **Date** | Timestamp when the job completed (null if still processing) | 



## Enum: StatusEnum


* `processing` (value: `"processing"`)

* `completed` (value: `"completed"`)

* `error` (value: `"error"`)




