# QueryNlGet200ResponseSeriesInnerEntity

The entity that this observation refers to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the entity | [optional] 
**name** | **str** | Human-readable name of the entity | 

## Example

```python
from qoery.models.query_nl_get200_response_series_inner_entity import QueryNlGet200ResponseSeriesInnerEntity

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlGet200ResponseSeriesInnerEntity from a JSON string
query_nl_get200_response_series_inner_entity_instance = QueryNlGet200ResponseSeriesInnerEntity.from_json(json)
# print the JSON string representation of the object
print(QueryNlGet200ResponseSeriesInnerEntity.to_json())

# convert the object into a dict
query_nl_get200_response_series_inner_entity_dict = query_nl_get200_response_series_inner_entity_instance.to_dict()
# create an instance of QueryNlGet200ResponseSeriesInnerEntity from a dict
query_nl_get200_response_series_inner_entity_from_dict = QueryNlGet200ResponseSeriesInnerEntity.from_dict(query_nl_get200_response_series_inner_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


