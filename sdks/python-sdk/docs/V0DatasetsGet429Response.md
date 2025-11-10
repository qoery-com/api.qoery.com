# V0DatasetsGet429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message | 
**status** | **int** | HTTP status code | 
**details** | **str** | Additional error details | [optional] 
**reset_date** | **datetime** | Date when the quota resets | [optional] 

## Example

```python
from qoery.models.v0_datasets_get429_response import V0DatasetsGet429Response

# TODO update the JSON string below
json = "{}"
# create an instance of V0DatasetsGet429Response from a JSON string
v0_datasets_get429_response_instance = V0DatasetsGet429Response.from_json(json)
# print the JSON string representation of the object
print(V0DatasetsGet429Response.to_json())

# convert the object into a dict
v0_datasets_get429_response_dict = v0_datasets_get429_response_instance.to_dict()
# create an instance of V0DatasetsGet429Response from a dict
v0_datasets_get429_response_from_dict = V0DatasetsGet429Response.from_dict(v0_datasets_get429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


