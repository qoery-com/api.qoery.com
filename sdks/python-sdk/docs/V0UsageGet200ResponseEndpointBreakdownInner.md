# V0UsageGet200ResponseEndpointBreakdownInner

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
from qoery.models.v0_usage_get200_response_endpoint_breakdown_inner import V0UsageGet200ResponseEndpointBreakdownInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0UsageGet200ResponseEndpointBreakdownInner from a JSON string
v0_usage_get200_response_endpoint_breakdown_inner_instance = V0UsageGet200ResponseEndpointBreakdownInner.from_json(json)
# print the JSON string representation of the object
print(V0UsageGet200ResponseEndpointBreakdownInner.to_json())

# convert the object into a dict
v0_usage_get200_response_endpoint_breakdown_inner_dict = v0_usage_get200_response_endpoint_breakdown_inner_instance.to_dict()
# create an instance of V0UsageGet200ResponseEndpointBreakdownInner from a dict
v0_usage_get200_response_endpoint_breakdown_inner_from_dict = V0UsageGet200ResponseEndpointBreakdownInner.from_dict(v0_usage_get200_response_endpoint_breakdown_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


