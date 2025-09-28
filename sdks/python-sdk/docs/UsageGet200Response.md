# UsageGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries_used** | **int** | Number of queries used in current period | 
**queries_limit** | **int** | Maximum queries allowed in current period | 
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 
**concurrent_requests** | **int** | Current number of concurrent requests | 
**max_concurrent** | **int** | Maximum concurrent requests allowed | 

## Example

```python
from openapi_client.models.usage_get200_response import UsageGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsageGet200Response from a JSON string
usage_get200_response_instance = UsageGet200Response.from_json(json)
# print the JSON string representation of the object
print(UsageGet200Response.to_json())

# convert the object into a dict
usage_get200_response_dict = usage_get200_response_instance.to_dict()
# create an instance of UsageGet200Response from a dict
usage_get200_response_from_dict = UsageGet200Response.from_dict(usage_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


