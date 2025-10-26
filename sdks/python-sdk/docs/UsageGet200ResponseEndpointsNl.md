# UsageGet200ResponseEndpointsNl

Usage statistics for a specific endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calls_used** | **int** | Number of calls used in current period | 
**calls_limit** | **str** | Maximum calls allowed in current period (returned as string) | 
**tokens_in** | **int** | Total input tokens consumed in current period | 
**tokens_out** | **int** | Total output tokens consumed in current period | 
**errors** | **int** | Total number of errors in current period | 
**remaining** | **int** | Number of calls remaining in current period | 

## Example

```python
from qoery.models.usage_get200_response_endpoints_nl import UsageGet200ResponseEndpointsNl

# TODO update the JSON string below
json = "{}"
# create an instance of UsageGet200ResponseEndpointsNl from a JSON string
usage_get200_response_endpoints_nl_instance = UsageGet200ResponseEndpointsNl.from_json(json)
# print the JSON string representation of the object
print(UsageGet200ResponseEndpointsNl.to_json())

# convert the object into a dict
usage_get200_response_endpoints_nl_dict = usage_get200_response_endpoints_nl_instance.to_dict()
# create an instance of UsageGet200ResponseEndpointsNl from a dict
usage_get200_response_endpoints_nl_from_dict = UsageGet200ResponseEndpointsNl.from_dict(usage_get200_response_endpoints_nl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


