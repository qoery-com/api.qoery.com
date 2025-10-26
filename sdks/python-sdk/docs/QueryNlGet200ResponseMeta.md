# QueryNlGet200ResponseMeta

Metadata about query execution and pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_count** | **int** | Number of results returned in this response | 
**page** | [**QueryNlGet200ResponseMetaPage**](QueryNlGet200ResponseMetaPage.md) |  | [optional] 
**diagnostics** | **Dict[str, object]** | Additional diagnostic information about the query execution | [optional] 

## Example

```python
from qoery.models.query_nl_get200_response_meta import QueryNlGet200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlGet200ResponseMeta from a JSON string
query_nl_get200_response_meta_instance = QueryNlGet200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print(QueryNlGet200ResponseMeta.to_json())

# convert the object into a dict
query_nl_get200_response_meta_dict = query_nl_get200_response_meta_instance.to_dict()
# create an instance of QueryNlGet200ResponseMeta from a dict
query_nl_get200_response_meta_from_dict = QueryNlGet200ResponseMeta.from_dict(query_nl_get200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


