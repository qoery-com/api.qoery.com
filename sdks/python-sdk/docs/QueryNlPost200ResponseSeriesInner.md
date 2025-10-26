# QueryNlPost200ResponseSeriesInner

A logical group of observations sharing the same entity/metric/unit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the series | [optional] 
**name** | **str** | Human-readable name of the series | [optional] 
**entity** | [**QueryNlPost200ResponseSeriesInnerEntity**](QueryNlPost200ResponseSeriesInnerEntity.md) |  | 
**metric** | [**QueryNlPost200ResponseSeriesInnerMetric**](QueryNlPost200ResponseSeriesInnerMetric.md) |  | 
**unit** | [**QueryNlPost200ResponseSeriesInnerUnit**](QueryNlPost200ResponseSeriesInnerUnit.md) |  | [optional] 
**source** | [**QueryNlPost200ResponseSeriesInnerSource**](QueryNlPost200ResponseSeriesInnerSource.md) |  | 
**frequency** | **str** | Frequency of the time series (e.g., monthly, annual) | [optional] 
**description** | **str** | Description of the series | [optional] 
**labels** | **Dict[str, object]** | Additional labels and metadata at the series level | [optional] 
**observations** | [**List[QueryNlPost200ResponseSeriesInnerObservationsInner]**](QueryNlPost200ResponseSeriesInnerObservationsInner.md) | The ordered observations for this series | 

## Example

```python
from qoery.models.query_nl_post200_response_series_inner import QueryNlPost200ResponseSeriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlPost200ResponseSeriesInner from a JSON string
query_nl_post200_response_series_inner_instance = QueryNlPost200ResponseSeriesInner.from_json(json)
# print the JSON string representation of the object
print(QueryNlPost200ResponseSeriesInner.to_json())

# convert the object into a dict
query_nl_post200_response_series_inner_dict = query_nl_post200_response_series_inner_instance.to_dict()
# create an instance of QueryNlPost200ResponseSeriesInner from a dict
query_nl_post200_response_series_inner_from_dict = QueryNlPost200ResponseSeriesInner.from_dict(query_nl_post200_response_series_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


