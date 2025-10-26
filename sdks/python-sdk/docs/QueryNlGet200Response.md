# QueryNlGet200Response

Response from natural language query endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**List[QueryNlGet200ResponseSeriesInner]**](QueryNlGet200ResponseSeriesInner.md) | Array of series, each with its observations | 
**meta** | [**QueryNlGet200ResponseMeta**](QueryNlGet200ResponseMeta.md) |  | 
**description** | **str** | Natural language description of the query result | [optional] 

## Example

```python
from qoery.models.query_nl_get200_response import QueryNlGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlGet200Response from a JSON string
query_nl_get200_response_instance = QueryNlGet200Response.from_json(json)
# print the JSON string representation of the object
print(QueryNlGet200Response.to_json())

# convert the object into a dict
query_nl_get200_response_dict = query_nl_get200_response_instance.to_dict()
# create an instance of QueryNlGet200Response from a dict
query_nl_get200_response_from_dict = QueryNlGet200Response.from_dict(query_nl_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


