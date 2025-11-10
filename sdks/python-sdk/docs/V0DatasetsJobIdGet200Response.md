# V0DatasetsJobIdGet200Response

Complete status information for a dataset collection job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique identifier for the job | 
**status** | **str** | Current job status | 
**query** | **str** | Original search query | 
**progress** | [**V0DatasetsJobIdGet200ResponseProgress**](V0DatasetsJobIdGet200ResponseProgress.md) |  | 
**urls** | **List[str]** | List of URLs being processed | 
**csv_url** | **str** | URL to download the CSV file | 
**error** | **str** | Error message if status is &#39;error&#39; | 
**started_at** | **datetime** | Timestamp when the job started | 
**completed_at** | **datetime** | Timestamp when the job completed (null if still processing) | 

## Example

```python
from qoery.models.v0_datasets_job_id_get200_response import V0DatasetsJobIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V0DatasetsJobIdGet200Response from a JSON string
v0_datasets_job_id_get200_response_instance = V0DatasetsJobIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(V0DatasetsJobIdGet200Response.to_json())

# convert the object into a dict
v0_datasets_job_id_get200_response_dict = v0_datasets_job_id_get200_response_instance.to_dict()
# create an instance of V0DatasetsJobIdGet200Response from a dict
v0_datasets_job_id_get200_response_from_dict = V0DatasetsJobIdGet200Response.from_dict(v0_datasets_job_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


