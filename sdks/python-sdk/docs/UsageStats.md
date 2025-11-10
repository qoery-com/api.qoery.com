# UsageStats

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
from qoery.models.usage_stats import UsageStats

# TODO update the JSON string below
json = "{}"
# create an instance of UsageStats from a JSON string
usage_stats_instance = UsageStats.from_json(json)
# print the JSON string representation of the object
print(UsageStats.to_json())

# convert the object into a dict
usage_stats_dict = usage_stats_instance.to_dict()
# create an instance of UsageStats from a dict
usage_stats_from_dict = UsageStats.from_dict(usage_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


