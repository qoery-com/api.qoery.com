# V0DatasetsGet400Response

Standard error response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message | 
**status** | **int** | HTTP status code | 
**details** | **str** | Additional error details | [optional] 

## Example

```python
from qoery.models.v0_datasets_get400_response import V0DatasetsGet400Response

# TODO update the JSON string below
json = "{}"
# create an instance of V0DatasetsGet400Response from a JSON string
v0_datasets_get400_response_instance = V0DatasetsGet400Response.from_json(json)
# print the JSON string representation of the object
print(V0DatasetsGet400Response.to_json())

# convert the object into a dict
v0_datasets_get400_response_dict = v0_datasets_get400_response_instance.to_dict()
# create an instance of V0DatasetsGet400Response from a dict
v0_datasets_get400_response_from_dict = V0DatasetsGet400Response.from_dict(v0_datasets_get400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


