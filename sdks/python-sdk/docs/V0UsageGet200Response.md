# V0UsageGet200Response

Complete usage statistics for a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User identifier | 
**plan** | **str** | Current subscription plan | 
**total_usage** | **int** | Total number of API calls across all endpoints | 
**total_errors** | **int** | Total number of errors across all endpoints | 
**endpoint_breakdown** | [**List[V0UsageGet200ResponseEndpointBreakdownInner]**](V0UsageGet200ResponseEndpointBreakdownInner.md) | Usage breakdown by endpoint | 

## Example

```python
from qoery.models.v0_usage_get200_response import V0UsageGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V0UsageGet200Response from a JSON string
v0_usage_get200_response_instance = V0UsageGet200Response.from_json(json)
# print the JSON string representation of the object
print(V0UsageGet200Response.to_json())

# convert the object into a dict
v0_usage_get200_response_dict = v0_usage_get200_response_instance.to_dict()
# create an instance of V0UsageGet200Response from a dict
v0_usage_get200_response_from_dict = V0UsageGet200Response.from_dict(v0_usage_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


