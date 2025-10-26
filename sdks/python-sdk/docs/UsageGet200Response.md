# UsageGet200Response

Usage statistics per endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** | Start of the current usage period | 
**period_end** | **datetime** | End of the current usage period | 
**plan** | **str** | Current subscription plan | 
**endpoints** | [**UsageGet200ResponseEndpoints**](UsageGet200ResponseEndpoints.md) |  | 

## Example

```python
from qoery.models.usage_get200_response import UsageGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsageGet200Response from a JSON string
usage_get200_response_instance = UsageGet200Response.from_json(json)
# print the JSON string representation of the object
print(UsageGet200Response.to_json())

# convert the object into a dict
usage_get200_response_dict = usage_get200_response_instance.to_dict()
# create an instance of UsageGet200Response from a dict
usage_get200_response_from_dict = UsageGet200Response.from_dict(usage_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


