# UsageGet200ResponseEndpoints

Usage statistics broken down by endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nl** | [**UsageGet200ResponseEndpointsNl**](UsageGet200ResponseEndpointsNl.md) |  | 
**scrape** | [**UsageGet200ResponseEndpointsNl**](UsageGet200ResponseEndpointsNl.md) |  | 

## Example

```python
from qoery.models.usage_get200_response_endpoints import UsageGet200ResponseEndpoints

# TODO update the JSON string below
json = "{}"
# create an instance of UsageGet200ResponseEndpoints from a JSON string
usage_get200_response_endpoints_instance = UsageGet200ResponseEndpoints.from_json(json)
# print the JSON string representation of the object
print(UsageGet200ResponseEndpoints.to_json())

# convert the object into a dict
usage_get200_response_endpoints_dict = usage_get200_response_endpoints_instance.to_dict()
# create an instance of UsageGet200ResponseEndpoints from a dict
usage_get200_response_endpoints_from_dict = UsageGet200ResponseEndpoints.from_dict(usage_get200_response_endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


