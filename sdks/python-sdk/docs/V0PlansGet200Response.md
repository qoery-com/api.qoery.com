# V0PlansGet200Response

Response containing all available plans

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plans** | [**Dict[str, V0PlansGet200ResponsePlansValue]**](V0PlansGet200ResponsePlansValue.md) | Plans keyed by plan name | 
**default_plan** | **str** | Default plan name | 

## Example

```python
from qoery.models.v0_plans_get200_response import V0PlansGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V0PlansGet200Response from a JSON string
v0_plans_get200_response_instance = V0PlansGet200Response.from_json(json)
# print the JSON string representation of the object
print(V0PlansGet200Response.to_json())

# convert the object into a dict
v0_plans_get200_response_dict = v0_plans_get200_response_instance.to_dict()
# create an instance of V0PlansGet200Response from a dict
v0_plans_get200_response_from_dict = V0PlansGet200Response.from_dict(v0_plans_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


