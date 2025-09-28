# NLQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 

## Example

```python
from openapi_client.models.nl_query_request import NLQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NLQueryRequest from a JSON string
nl_query_request_instance = NLQueryRequest.from_json(json)
# print the JSON string representation of the object
print(NLQueryRequest.to_json())

# convert the object into a dict
nl_query_request_dict = nl_query_request_instance.to_dict()
# create an instance of NLQueryRequest from a dict
nl_query_request_from_dict = NLQueryRequest.from_dict(nl_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


