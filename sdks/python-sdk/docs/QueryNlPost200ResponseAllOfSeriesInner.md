# QueryNlPost200ResponseAllOfSeriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_id** | **str** | short id for the series (optional but recommended) | [optional] 
**name** | **str** | human-friendly name for the series | 
**unit** | **str** | unit of measurement (optional) | [optional] 
**observations** | [**List[QueryNlPost200ResponseAllOfSeriesInnerObservationsInner]**](QueryNlPost200ResponseAllOfSeriesInnerObservationsInner.md) |  | 

## Example

```python
from qoery.models.query_nl_post200_response_all_of_series_inner import QueryNlPost200ResponseAllOfSeriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlPost200ResponseAllOfSeriesInner from a JSON string
query_nl_post200_response_all_of_series_inner_instance = QueryNlPost200ResponseAllOfSeriesInner.from_json(json)
# print the JSON string representation of the object
print(QueryNlPost200ResponseAllOfSeriesInner.to_json())

# convert the object into a dict
query_nl_post200_response_all_of_series_inner_dict = query_nl_post200_response_all_of_series_inner_instance.to_dict()
# create an instance of QueryNlPost200ResponseAllOfSeriesInner from a dict
query_nl_post200_response_all_of_series_inner_from_dict = QueryNlPost200ResponseAllOfSeriesInner.from_dict(query_nl_post200_response_all_of_series_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


