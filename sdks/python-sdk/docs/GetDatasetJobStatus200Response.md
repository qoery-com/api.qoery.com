# GetDatasetJobStatus200Response

Complete status information for a dataset collection job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique identifier for the job | 
**status** | **str** | Current job status. Possible values: - &#x60;processing&#x60;: Job is actively collecting and processing data - &#x60;completed&#x60;: Job finished successfully, CSV is ready for download - &#x60;error&#x60;: Job failed, check the &#x60;error&#x60; field for details  | 
**query** | **str** | Original search query | 
**progress** | [**GetDatasetJobStatus200ResponseProgress**](GetDatasetJobStatus200ResponseProgress.md) |  | 
**urls** | **List[str]** | List of URLs being processed | 
**csv_url** | **str** | URL to download the CSV file | 
**error** | **str** | Error message if status is &#39;error&#39; (only present when status is &#39;error&#39;) | [optional] 
**started_at** | **datetime** | Timestamp when the job started | 
**completed_at** | **datetime** | Timestamp when the job completed (only present when status is &#39;completed&#39;) | [optional] 

## Example

```python
from qoery.models.get_dataset_job_status200_response import GetDatasetJobStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatasetJobStatus200Response from a JSON string
get_dataset_job_status200_response_instance = GetDatasetJobStatus200Response.from_json(json)
# print the JSON string representation of the object
print(GetDatasetJobStatus200Response.to_json())

# convert the object into a dict
get_dataset_job_status200_response_dict = get_dataset_job_status200_response_instance.to_dict()
# create an instance of GetDatasetJobStatus200Response from a dict
get_dataset_job_status200_response_from_dict = GetDatasetJobStatus200Response.from_dict(get_dataset_job_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


