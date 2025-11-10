# ListPlans200ResponsePlansValueMonthlyPrice

Monthly pricing option

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Price amount | 
**currency** | **str** | Currency code | 
**price_id** | **str** | Stripe price ID | 

## Example

```python
from qoery.models.list_plans200_response_plans_value_monthly_price import ListPlans200ResponsePlansValueMonthlyPrice

# TODO update the JSON string below
json = "{}"
# create an instance of ListPlans200ResponsePlansValueMonthlyPrice from a JSON string
list_plans200_response_plans_value_monthly_price_instance = ListPlans200ResponsePlansValueMonthlyPrice.from_json(json)
# print the JSON string representation of the object
print(ListPlans200ResponsePlansValueMonthlyPrice.to_json())

# convert the object into a dict
list_plans200_response_plans_value_monthly_price_dict = list_plans200_response_plans_value_monthly_price_instance.to_dict()
# create an instance of ListPlans200ResponsePlansValueMonthlyPrice from a dict
list_plans200_response_plans_value_monthly_price_from_dict = ListPlans200ResponsePlansValueMonthlyPrice.from_dict(list_plans200_response_plans_value_monthly_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


