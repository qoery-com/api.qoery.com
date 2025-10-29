# PlansGet200ResponsePlansValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**price** | **str** | Human-friendly display price | [optional] 
**billing** | **str** | Billing cadence for display (e.g., monthly, annual, one-time) | [optional] 
**limits** | **Dict[str, int]** | Monthly limits keyed by endpoint (e.g., &#39;query/nl&#39;, &#39;scrape&#39;, &#39;plot2table&#39;) | [optional] 
**api_keys** | [**PlansGet200ResponsePlansValueApiKeys**](PlansGet200ResponsePlansValueApiKeys.md) |  | [optional] 
**support** | **str** |  | [optional] 
**monthly_price** | [**PlansGet200ResponsePlansValueMonthlyPrice**](PlansGet200ResponsePlansValueMonthlyPrice.md) |  | [optional] 
**annual_price** | [**PlansGet200ResponsePlansValueMonthlyPrice**](PlansGet200ResponsePlansValueMonthlyPrice.md) |  | [optional] 
**discount_percentage** | **float** |  | [optional] 

## Example

```python
from qoery.models.plans_get200_response_plans_value import PlansGet200ResponsePlansValue

# TODO update the JSON string below
json = "{}"
# create an instance of PlansGet200ResponsePlansValue from a JSON string
plans_get200_response_plans_value_instance = PlansGet200ResponsePlansValue.from_json(json)
# print the JSON string representation of the object
print(PlansGet200ResponsePlansValue.to_json())

# convert the object into a dict
plans_get200_response_plans_value_dict = plans_get200_response_plans_value_instance.to_dict()
# create an instance of PlansGet200ResponsePlansValue from a dict
plans_get200_response_plans_value_from_dict = PlansGet200ResponsePlansValue.from_dict(plans_get200_response_plans_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


