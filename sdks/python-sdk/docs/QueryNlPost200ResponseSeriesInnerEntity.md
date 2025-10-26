# QueryNlPost200ResponseSeriesInnerEntity

The entity that this observation refers to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the entity | [optional] 
**name** | **str** | Human-readable name of the entity | 

## Example

```python
from qoery.models.query_nl_post200_response_series_inner_entity import QueryNlPost200ResponseSeriesInnerEntity

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlPost200ResponseSeriesInnerEntity from a JSON string
query_nl_post200_response_series_inner_entity_instance = QueryNlPost200ResponseSeriesInnerEntity.from_json(json)
# print the JSON string representation of the object
print(QueryNlPost200ResponseSeriesInnerEntity.to_json())

# convert the object into a dict
query_nl_post200_response_series_inner_entity_dict = query_nl_post200_response_series_inner_entity_instance.to_dict()
# create an instance of QueryNlPost200ResponseSeriesInnerEntity from a dict
query_nl_post200_response_series_inner_entity_from_dict = QueryNlPost200ResponseSeriesInnerEntity.from_dict(query_nl_post200_response_series_inner_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


