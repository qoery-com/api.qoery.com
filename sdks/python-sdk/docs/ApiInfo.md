# ApiInfo

API information and available endpoints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**endpoints** | **Dict[str, str]** | Available endpoint descriptions | 

## Example

```python
from qoery.models.api_info import ApiInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInfo from a JSON string
api_info_instance = ApiInfo.from_json(json)
# print the JSON string representation of the object
print(ApiInfo.to_json())

# convert the object into a dict
api_info_dict = api_info_instance.to_dict()
# create an instance of ApiInfo from a dict
api_info_from_dict = ApiInfo.from_dict(api_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


