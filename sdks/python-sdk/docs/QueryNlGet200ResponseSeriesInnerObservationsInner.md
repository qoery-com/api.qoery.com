# QueryNlGet200ResponseSeriesInnerObservationsInner

A single data point within a specific series

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **str** | The dimension/axis value (timestamp for time series, category for categorical data, x-value for scatter plots, etc.) | 
**value** | [**QueryNlGet200ResponseSeriesInnerObservationsInnerValue**](QueryNlGet200ResponseSeriesInnerObservationsInnerValue.md) |  | 

## Example

```python
from qoery.models.query_nl_get200_response_series_inner_observations_inner import QueryNlGet200ResponseSeriesInnerObservationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlGet200ResponseSeriesInnerObservationsInner from a JSON string
query_nl_get200_response_series_inner_observations_inner_instance = QueryNlGet200ResponseSeriesInnerObservationsInner.from_json(json)
# print the JSON string representation of the object
print(QueryNlGet200ResponseSeriesInnerObservationsInner.to_json())

# convert the object into a dict
query_nl_get200_response_series_inner_observations_inner_dict = query_nl_get200_response_series_inner_observations_inner_instance.to_dict()
# create an instance of QueryNlGet200ResponseSeriesInnerObservationsInner from a dict
query_nl_get200_response_series_inner_observations_inner_from_dict = QueryNlGet200ResponseSeriesInnerObservationsInner.from_dict(query_nl_get200_response_series_inner_observations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


