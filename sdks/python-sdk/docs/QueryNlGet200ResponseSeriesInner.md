# QueryNlGet200ResponseSeriesInner

A data series with observations from a specific source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the source page | 
**title** | **str** | Title of the series | 
**url_title** | **str** | Title from the URL/source | 
**observations** | [**List[QueryNlGet200ResponseSeriesInnerObservationsInner]**](QueryNlGet200ResponseSeriesInnerObservationsInner.md) | The ordered observations for this series | 
**relevance_score** | **float** | Relevance score for this series (0-1) | 

## Example

```python
from qoery.models.query_nl_get200_response_series_inner import QueryNlGet200ResponseSeriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlGet200ResponseSeriesInner from a JSON string
query_nl_get200_response_series_inner_instance = QueryNlGet200ResponseSeriesInner.from_json(json)
# print the JSON string representation of the object
print(QueryNlGet200ResponseSeriesInner.to_json())

# convert the object into a dict
query_nl_get200_response_series_inner_dict = query_nl_get200_response_series_inner_instance.to_dict()
# create an instance of QueryNlGet200ResponseSeriesInner from a dict
query_nl_get200_response_series_inner_from_dict = QueryNlGet200ResponseSeriesInner.from_dict(query_nl_get200_response_series_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


