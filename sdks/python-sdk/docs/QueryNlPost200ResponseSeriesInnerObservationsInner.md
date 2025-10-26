# QueryNlPost200ResponseSeriesInnerObservationsInner

A single timestamped value within a specific series

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Timestamp of the observation | 
**value** | [**QueryNlPost200ResponseSeriesInnerObservationsInnerValue**](QueryNlPost200ResponseSeriesInnerObservationsInnerValue.md) |  | 

## Example

```python
from qoery.models.query_nl_post200_response_series_inner_observations_inner import QueryNlPost200ResponseSeriesInnerObservationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlPost200ResponseSeriesInnerObservationsInner from a JSON string
query_nl_post200_response_series_inner_observations_inner_instance = QueryNlPost200ResponseSeriesInnerObservationsInner.from_json(json)
# print the JSON string representation of the object
print(QueryNlPost200ResponseSeriesInnerObservationsInner.to_json())

# convert the object into a dict
query_nl_post200_response_series_inner_observations_inner_dict = query_nl_post200_response_series_inner_observations_inner_instance.to_dict()
# create an instance of QueryNlPost200ResponseSeriesInnerObservationsInner from a dict
query_nl_post200_response_series_inner_observations_inner_from_dict = QueryNlPost200ResponseSeriesInnerObservationsInner.from_dict(query_nl_post200_response_series_inner_observations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


