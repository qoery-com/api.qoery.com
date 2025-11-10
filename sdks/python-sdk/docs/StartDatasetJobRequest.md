# StartDatasetJobRequest

Request to start a new dataset collection job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Search query for dataset collection | 

## Example

```python
from qoery.models.start_dataset_job_request import StartDatasetJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartDatasetJobRequest from a JSON string
start_dataset_job_request_instance = StartDatasetJobRequest.from_json(json)
# print the JSON string representation of the object
print(StartDatasetJobRequest.to_json())

# convert the object into a dict
start_dataset_job_request_dict = start_dataset_job_request_instance.to_dict()
# create an instance of StartDatasetJobRequest from a dict
start_dataset_job_request_from_dict = StartDatasetJobRequest.from_dict(start_dataset_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


