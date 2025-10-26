# QueryNlPost200ResponseMetaPage

Pagination information for the response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Number of items requested per page | 
**offset** | **int** | Offset index of the first item in this page | 
**next_cursor** | **str** | Opaque token to fetch the next page | [optional] 
**has_more** | **bool** | Whether there are more items available beyond this page | 

## Example

```python
from qoery.models.query_nl_post200_response_meta_page import QueryNlPost200ResponseMetaPage

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlPost200ResponseMetaPage from a JSON string
query_nl_post200_response_meta_page_instance = QueryNlPost200ResponseMetaPage.from_json(json)
# print the JSON string representation of the object
print(QueryNlPost200ResponseMetaPage.to_json())

# convert the object into a dict
query_nl_post200_response_meta_page_dict = query_nl_post200_response_meta_page_instance.to_dict()
# create an instance of QueryNlPost200ResponseMetaPage from a dict
query_nl_post200_response_meta_page_from_dict = QueryNlPost200ResponseMetaPage.from_dict(query_nl_post200_response_meta_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


