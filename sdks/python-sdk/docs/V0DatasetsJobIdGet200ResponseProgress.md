# V0DatasetsJobIdGet200ResponseProgress

Progress information for a dataset collection job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_step** | **str** | Current step in the processing pipeline | 
**rows_collected** | **int** | Number of data rows collected so far | 
**urls_processed** | **int** | Number of URLs processed so far | 
**urls_total** | **int** | Total number of URLs to process | 
**last_updated** | **datetime** | Timestamp of last progress update | 

## Example

```python
from qoery.models.v0_datasets_job_id_get200_response_progress import V0DatasetsJobIdGet200ResponseProgress

# TODO update the JSON string below
json = "{}"
# create an instance of V0DatasetsJobIdGet200ResponseProgress from a JSON string
v0_datasets_job_id_get200_response_progress_instance = V0DatasetsJobIdGet200ResponseProgress.from_json(json)
# print the JSON string representation of the object
print(V0DatasetsJobIdGet200ResponseProgress.to_json())

# convert the object into a dict
v0_datasets_job_id_get200_response_progress_dict = v0_datasets_job_id_get200_response_progress_instance.to_dict()
# create an instance of V0DatasetsJobIdGet200ResponseProgress from a dict
v0_datasets_job_id_get200_response_progress_from_dict = V0DatasetsJobIdGet200ResponseProgress.from_dict(v0_datasets_job_id_get200_response_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


