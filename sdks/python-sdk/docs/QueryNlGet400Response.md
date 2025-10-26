# QueryNlGet400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**code** | **int** |  | 
**message** | **str** | Additional error message | [optional] 
**details** | **str** |  | [optional] 

## Example

```python
from qoery.models.query_nl_get400_response import QueryNlGet400Response

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlGet400Response from a JSON string
query_nl_get400_response_instance = QueryNlGet400Response.from_json(json)
# print the JSON string representation of the object
print(QueryNlGet400Response.to_json())

# convert the object into a dict
query_nl_get400_response_dict = query_nl_get400_response_instance.to_dict()
# create an instance of QueryNlGet400Response from a dict
query_nl_get400_response_from_dict = QueryNlGet400Response.from_dict(query_nl_get400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


