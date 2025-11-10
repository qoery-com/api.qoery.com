# EndpointUsage

Usage statistics for a specific endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Endpoint path | 
**calls** | **int** | Number of calls made in the current period | 
**errors** | **int** | Number of errors encountered | 
**limit** | **int** | Monthly limit for this endpoint | 

## Example

```python
from qoery.models.endpoint_usage import EndpointUsage

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointUsage from a JSON string
endpoint_usage_instance = EndpointUsage.from_json(json)
# print the JSON string representation of the object
print(EndpointUsage.to_json())

# convert the object into a dict
endpoint_usage_dict = endpoint_usage_instance.to_dict()
# create an instance of EndpointUsage from a dict
endpoint_usage_from_dict = EndpointUsage.from_dict(endpoint_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


