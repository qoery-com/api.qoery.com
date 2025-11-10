# Plan

Subscription plan details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Plan display name | 
**description** | **str** | Plan description | 
**price** | **str** | Human-friendly display price | 
**billing** | **str** | Billing cadence description | 
**limits** | **Dict[str, int]** | Monthly limits per endpoint | 
**api_keys** | [**ListPlans200ResponsePlansValueApiKeys**](ListPlans200ResponsePlansValueApiKeys.md) |  | 
**support** | **str** | Support level provided with this plan. Possible values: - &#x60;Community&#x60;: Community support via forums and documentation - &#x60;Standard&#x60;: Standard email support with 48-hour response time - &#x60;Priority&#x60;: Priority support with 24-hour response time  | 
**monthly_price** | [**ListPlans200ResponsePlansValueMonthlyPrice**](ListPlans200ResponsePlansValueMonthlyPrice.md) |  | [optional] 
**annual_price** | [**ListPlans200ResponsePlansValueAnnualPrice**](ListPlans200ResponsePlansValueAnnualPrice.md) |  | [optional] 
**discount_percentage** | **float** | Discount percentage for annual billing | [optional] 

## Example

```python
from qoery.models.plan import Plan

# TODO update the JSON string below
json = "{}"
# create an instance of Plan from a JSON string
plan_instance = Plan.from_json(json)
# print the JSON string representation of the object
print(Plan.to_json())

# convert the object into a dict
plan_dict = plan_instance.to_dict()
# create an instance of Plan from a dict
plan_from_dict = Plan.from_dict(plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


