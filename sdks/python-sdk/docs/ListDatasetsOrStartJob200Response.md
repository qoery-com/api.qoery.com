# ListDatasetsOrStartJob200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**endpoints** | **Dict[str, str]** | Available endpoint descriptions | 
**job_id** | **str** | Unique identifier for the job | 
**status** | **str** | Initial job status | 
**polling_interval_ms** | **int** | Recommended polling interval in milliseconds | 

## Example

```python
from qoery.models.list_datasets_or_start_job200_response import ListDatasetsOrStartJob200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatasetsOrStartJob200Response from a JSON string
list_datasets_or_start_job200_response_instance = ListDatasetsOrStartJob200Response.from_json(json)
# print the JSON string representation of the object
print(ListDatasetsOrStartJob200Response.to_json())

# convert the object into a dict
list_datasets_or_start_job200_response_dict = list_datasets_or_start_job200_response_instance.to_dict()
# create an instance of ListDatasetsOrStartJob200Response from a dict
list_datasets_or_start_job200_response_from_dict = ListDatasetsOrStartJob200Response.from_dict(list_datasets_or_start_job200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


