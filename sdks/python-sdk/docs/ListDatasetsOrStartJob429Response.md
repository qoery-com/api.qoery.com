# ListDatasetsOrStartJob429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message | 
**status** | **int** | HTTP status code (may be omitted in some error responses) | [optional] 
**details** | **str** | Additional error details (optional) | [optional] 
**reset_date** | **datetime** | Date when the quota resets | [optional] 

## Example

```python
from qoery.models.list_datasets_or_start_job429_response import ListDatasetsOrStartJob429Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatasetsOrStartJob429Response from a JSON string
list_datasets_or_start_job429_response_instance = ListDatasetsOrStartJob429Response.from_json(json)
# print the JSON string representation of the object
print(ListDatasetsOrStartJob429Response.to_json())

# convert the object into a dict
list_datasets_or_start_job429_response_dict = list_datasets_or_start_job429_response_instance.to_dict()
# create an instance of ListDatasetsOrStartJob429Response from a dict
list_datasets_or_start_job429_response_from_dict = ListDatasetsOrStartJob429Response.from_dict(list_datasets_or_start_job429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


