# QueryNlPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**List[QueryNlPost200ResponseAllOfSeriesInner]**](QueryNlPost200ResponseAllOfSeriesInner.md) |  | 
**sql_query** | **str** |  | 

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


