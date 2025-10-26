# QueryNlPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Natural language query | 

## Example

```python
from qoery.models.query_nl_post_request import QueryNlPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlPostRequest from a JSON string
query_nl_post_request_instance = QueryNlPostRequest.from_json(json)
# print the JSON string representation of the object
print(QueryNlPostRequest.to_json())

# convert the object into a dict
query_nl_post_request_dict = query_nl_post_request_instance.to_dict()
# create an instance of QueryNlPostRequest from a dict
query_nl_post_request_from_dict = QueryNlPostRequest.from_dict(query_nl_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


