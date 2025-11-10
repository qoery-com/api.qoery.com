# ListPlans200Response

Response containing all available plans

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plans** | [**Dict[str, ListPlans200ResponsePlansValue]**](ListPlans200ResponsePlansValue.md) | Plans keyed by plan name | 
**default_plan** | **str** | Default plan name | 

## Example

```python
from qoery.models.list_plans200_response import ListPlans200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPlans200Response from a JSON string
list_plans200_response_instance = ListPlans200Response.from_json(json)
# print the JSON string representation of the object
print(ListPlans200Response.to_json())

# convert the object into a dict
list_plans200_response_dict = list_plans200_response_instance.to_dict()
# create an instance of ListPlans200Response from a dict
list_plans200_response_from_dict = ListPlans200Response.from_dict(list_plans200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


