# JobStartRequest

Request to start a new dataset collection job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Search query for dataset collection | 

## Example

```python
from qoery.models.job_start_request import JobStartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobStartRequest from a JSON string
job_start_request_instance = JobStartRequest.from_json(json)
# print the JSON string representation of the object
print(JobStartRequest.to_json())

# convert the object into a dict
job_start_request_dict = job_start_request_instance.to_dict()
# create an instance of JobStartRequest from a dict
job_start_request_from_dict = JobStartRequest.from_dict(job_start_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


