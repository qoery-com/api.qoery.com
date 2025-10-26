# UsageStats

Usage statistics per endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** | Start of the current usage period | 
**period_end** | **datetime** | End of the current usage period | 
**plan** | **str** | Current subscription plan | 
**endpoints** | [**UsageStatsEndpoints**](UsageStatsEndpoints.md) |  | 

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


