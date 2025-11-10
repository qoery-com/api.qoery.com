# PlansResponse

Response containing all available plans

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plans** | [**Dict[str, ListPlans200ResponsePlansValue]**](ListPlans200ResponsePlansValue.md) | Plans keyed by plan name | 
**default_plan** | **str** | Default plan name | 

## Example

```python
from qoery.models.plans_response import PlansResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlansResponse from a JSON string
plans_response_instance = PlansResponse.from_json(json)
# print the JSON string representation of the object
print(PlansResponse.to_json())

# convert the object into a dict
plans_response_dict = plans_response_instance.to_dict()
# create an instance of PlansResponse from a dict
plans_response_from_dict = PlansResponse.from_dict(plans_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


