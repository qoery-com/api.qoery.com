# UsageStatsEndpoints

Usage statistics broken down by endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nl** | [**UsageStatsEndpointsNl**](UsageStatsEndpointsNl.md) |  | 
**scrape** | [**UsageStatsEndpointsNl**](UsageStatsEndpointsNl.md) |  | 
**plot2table** | [**UsageStatsEndpointsNl**](UsageStatsEndpointsNl.md) |  | 

## Example

```python
from qoery.models.usage_stats_endpoints import UsageStatsEndpoints

# TODO update the JSON string below
json = "{}"
# create an instance of UsageStatsEndpoints from a JSON string
usage_stats_endpoints_instance = UsageStatsEndpoints.from_json(json)
# print the JSON string representation of the object
print(UsageStatsEndpoints.to_json())

# convert the object into a dict
usage_stats_endpoints_dict = usage_stats_endpoints_instance.to_dict()
# create an instance of UsageStatsEndpoints from a dict
usage_stats_endpoints_from_dict = UsageStatsEndpoints.from_dict(usage_stats_endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


