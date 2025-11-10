# ListPlans200ResponsePlansValue

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
from qoery.models.list_plans200_response_plans_value import ListPlans200ResponsePlansValue

# TODO update the JSON string below
json = "{}"
# create an instance of ListPlans200ResponsePlansValue from a JSON string
list_plans200_response_plans_value_instance = ListPlans200ResponsePlansValue.from_json(json)
# print the JSON string representation of the object
print(ListPlans200ResponsePlansValue.to_json())

# convert the object into a dict
list_plans200_response_plans_value_dict = list_plans200_response_plans_value_instance.to_dict()
# create an instance of ListPlans200ResponsePlansValue from a dict
list_plans200_response_plans_value_from_dict = ListPlans200ResponsePlansValue.from_dict(list_plans200_response_plans_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


