# V0PlansGet200ResponsePlansValue

Subscription plan details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Plan display name | 
**description** | **str** | Plan description | 
**price** | **str** | Human-friendly display price | 
**billing** | **str** | Billing cadence description | 
**limits** | **Dict[str, int]** | Monthly limits per endpoint | 
**api_keys** | [**V0PlansGet200ResponsePlansValueApiKeys**](V0PlansGet200ResponsePlansValueApiKeys.md) |  | 
**support** | **str** | Support level | 
**monthly_price** | [**V0PlansGet200ResponsePlansValueMonthlyPrice**](V0PlansGet200ResponsePlansValueMonthlyPrice.md) |  | [optional] 
**annual_price** | [**V0PlansGet200ResponsePlansValueAnnualPrice**](V0PlansGet200ResponsePlansValueAnnualPrice.md) |  | [optional] 
**discount_percentage** | **float** | Discount percentage for annual billing | [optional] 

## Example

```python
from qoery.models.v0_plans_get200_response_plans_value import V0PlansGet200ResponsePlansValue

# TODO update the JSON string below
json = "{}"
# create an instance of V0PlansGet200ResponsePlansValue from a JSON string
v0_plans_get200_response_plans_value_instance = V0PlansGet200ResponsePlansValue.from_json(json)
# print the JSON string representation of the object
print(V0PlansGet200ResponsePlansValue.to_json())

# convert the object into a dict
v0_plans_get200_response_plans_value_dict = v0_plans_get200_response_plans_value_instance.to_dict()
# create an instance of V0PlansGet200ResponsePlansValue from a dict
v0_plans_get200_response_plans_value_from_dict = V0PlansGet200ResponsePlansValue.from_dict(v0_plans_get200_response_plans_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


