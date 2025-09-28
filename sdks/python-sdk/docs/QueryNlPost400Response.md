# QueryNlPost400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**code** | **int** |  | 
**details** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.query_nl_post400_response import QueryNlPost400Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlPost400Response from a JSON string
query_nl_post400_response_instance = QueryNlPost400Response.from_json(json)
# print the JSON string representation of the object
print(QueryNlPost400Response.to_json())

# convert the object into a dict
query_nl_post400_response_dict = query_nl_post400_response_instance.to_dict()
# create an instance of QueryNlPost400Response from a dict
query_nl_post400_response_from_dict = QueryNlPost400Response.from_dict(query_nl_post400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


