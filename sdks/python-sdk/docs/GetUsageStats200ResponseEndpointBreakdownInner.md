# GetUsageStats200ResponseEndpointBreakdownInner

Usage statistics for a specific endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Endpoint path | 
**calls** | **int** | Number of calls made in the current period | 
**errors** | **int** | Number of errors encountered | 
**limit** | **int** | Monthly limit for this endpoint | 

## Example

```python
from qoery.models.get_usage_stats200_response_endpoint_breakdown_inner import GetUsageStats200ResponseEndpointBreakdownInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsageStats200ResponseEndpointBreakdownInner from a JSON string
get_usage_stats200_response_endpoint_breakdown_inner_instance = GetUsageStats200ResponseEndpointBreakdownInner.from_json(json)
# print the JSON string representation of the object
print(GetUsageStats200ResponseEndpointBreakdownInner.to_json())

# convert the object into a dict
get_usage_stats200_response_endpoint_breakdown_inner_dict = get_usage_stats200_response_endpoint_breakdown_inner_instance.to_dict()
# create an instance of GetUsageStats200ResponseEndpointBreakdownInner from a dict
get_usage_stats200_response_endpoint_breakdown_inner_from_dict = GetUsageStats200ResponseEndpointBreakdownInner.from_dict(get_usage_stats200_response_endpoint_breakdown_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


