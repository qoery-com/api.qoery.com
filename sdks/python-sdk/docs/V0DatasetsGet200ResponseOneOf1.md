# V0DatasetsGet200ResponseOneOf1

Response when a job is started

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Unique identifier for the job | 
**status** | **str** | Initial job status | 
**polling_interval_ms** | **int** | Recommended polling interval in milliseconds | 

## Example

```python
from qoery.models.v0_datasets_get200_response_one_of1 import V0DatasetsGet200ResponseOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of V0DatasetsGet200ResponseOneOf1 from a JSON string
v0_datasets_get200_response_one_of1_instance = V0DatasetsGet200ResponseOneOf1.from_json(json)
# print the JSON string representation of the object
print(V0DatasetsGet200ResponseOneOf1.to_json())

# convert the object into a dict
v0_datasets_get200_response_one_of1_dict = v0_datasets_get200_response_one_of1_instance.to_dict()
# create an instance of V0DatasetsGet200ResponseOneOf1 from a dict
v0_datasets_get200_response_one_of1_from_dict = V0DatasetsGet200ResponseOneOf1.from_dict(v0_datasets_get200_response_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


