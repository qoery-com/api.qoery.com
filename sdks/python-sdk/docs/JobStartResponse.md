# JobStartResponse

Response when a job is started

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique identifier for the job | 
**status** | **str** | Initial job status | 
**polling_interval_ms** | **int** | Recommended polling interval in milliseconds | 

## Example

```python
from qoery.models.job_start_response import JobStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobStartResponse from a JSON string
job_start_response_instance = JobStartResponse.from_json(json)
# print the JSON string representation of the object
print(JobStartResponse.to_json())

# convert the object into a dict
job_start_response_dict = job_start_response_instance.to_dict()
# create an instance of JobStartResponse from a dict
job_start_response_from_dict = JobStartResponse.from_dict(job_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


