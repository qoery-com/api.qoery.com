# GetUsageStats200Response

Complete usage statistics for a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User identifier | 
**plan** | **str** | Current subscription plan. Possible values: - &#x60;free&#x60;: Free tier with basic limits - &#x60;starter&#x60;: Starter plan for small projects - &#x60;pro&#x60;: Professional plan for production use - &#x60;growth&#x60;: Growth plan for large-scale operations  | 
**total_usage** | **int** | Total number of API calls across all endpoints | 
**total_errors** | **int** | Total number of errors across all endpoints | 
**endpoint_breakdown** | [**List[GetUsageStats200ResponseEndpointBreakdownInner]**](GetUsageStats200ResponseEndpointBreakdownInner.md) | Usage breakdown by endpoint | 

## Example

```python
from qoery.models.get_usage_stats200_response import GetUsageStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUsageStats200Response from a JSON string
get_usage_stats200_response_instance = GetUsageStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetUsageStats200Response.to_json())

# convert the object into a dict
get_usage_stats200_response_dict = get_usage_stats200_response_instance.to_dict()
# create an instance of GetUsageStats200Response from a dict
get_usage_stats200_response_from_dict = GetUsageStats200Response.from_dict(get_usage_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


