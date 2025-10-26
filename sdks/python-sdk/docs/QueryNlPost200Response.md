# QueryNlPost200Response

Response from natural language query endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**List[QueryNlPost200ResponseSeriesInner]**](QueryNlPost200ResponseSeriesInner.md) | Array of series, each with its observations | 
**meta** | [**QueryNlPost200ResponseMeta**](QueryNlPost200ResponseMeta.md) |  | 
**description** | **str** | Natural language description of the query result | [optional] 

## Example

```python
from qoery.models.query_nl_post200_response import QueryNlPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlPost200Response from a JSON string
query_nl_post200_response_instance = QueryNlPost200Response.from_json(json)
# print the JSON string representation of the object
print(QueryNlPost200Response.to_json())

# convert the object into a dict
query_nl_post200_response_dict = query_nl_post200_response_instance.to_dict()
# create an instance of QueryNlPost200Response from a dict
query_nl_post200_response_from_dict = QueryNlPost200Response.from_dict(query_nl_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


