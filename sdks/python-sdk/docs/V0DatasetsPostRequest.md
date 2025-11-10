# V0DatasetsPostRequest

Request to start a new dataset collection job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | **str** | Search query for dataset collection | 

## Example

```python
from qoery.models.v0_datasets_post_request import V0DatasetsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V0DatasetsPostRequest from a JSON string
v0_datasets_post_request_instance = V0DatasetsPostRequest.from_json(json)
# print the JSON string representation of the object
print(V0DatasetsPostRequest.to_json())

# convert the object into a dict
v0_datasets_post_request_dict = v0_datasets_post_request_instance.to_dict()
# create an instance of V0DatasetsPostRequest from a dict
v0_datasets_post_request_from_dict = V0DatasetsPostRequest.from_dict(v0_datasets_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


