# QueryNlPost200ResponseSeriesInnerUnit

The unit used for the observation value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the unit | [optional] 
**name** | **str** | Human-readable name of the unit | 
**symbol** | **str** | Symbol of the unit (e.g., $, %, kg) | [optional] 

## Example

```python
from qoery.models.query_nl_post200_response_series_inner_unit import QueryNlPost200ResponseSeriesInnerUnit

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlPost200ResponseSeriesInnerUnit from a JSON string
query_nl_post200_response_series_inner_unit_instance = QueryNlPost200ResponseSeriesInnerUnit.from_json(json)
# print the JSON string representation of the object
print(QueryNlPost200ResponseSeriesInnerUnit.to_json())

# convert the object into a dict
query_nl_post200_response_series_inner_unit_dict = query_nl_post200_response_series_inner_unit_instance.to_dict()
# create an instance of QueryNlPost200ResponseSeriesInnerUnit from a dict
query_nl_post200_response_series_inner_unit_from_dict = QueryNlPost200ResponseSeriesInnerUnit.from_dict(query_nl_post200_response_series_inner_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


