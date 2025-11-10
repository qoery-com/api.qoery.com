# V0DatasetsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**endpoints** | **Dict[str, str]** | Available endpoint descriptions | 
**job_id** | **str** | Unique identifier for the job | 
**status** | **str** | Initial job status | 
**polling_interval_ms** | **int** | Recommended polling interval in milliseconds | 

## Example

```python
from qoery.models.v0_datasets_get200_response import V0DatasetsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V0DatasetsGet200Response from a JSON string
v0_datasets_get200_response_instance = V0DatasetsGet200Response.from_json(json)
# print the JSON string representation of the object
print(V0DatasetsGet200Response.to_json())

# convert the object into a dict
v0_datasets_get200_response_dict = v0_datasets_get200_response_instance.to_dict()
# create an instance of V0DatasetsGet200Response from a dict
v0_datasets_get200_response_from_dict = V0DatasetsGet200Response.from_dict(v0_datasets_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


