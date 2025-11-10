# Qoery.Plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Plan display name | 
**description** | **String** | Plan description | 
**price** | **String** | Human-friendly display price | 
**billing** | **String** | Billing cadence description | 
**limits** | **{String: Number}** | Monthly limits per endpoint | 
**apiKeys** | [**ListPlans200ResponsePlansValueApiKeys**](ListPlans200ResponsePlansValueApiKeys.md) |  | 
**support** | **String** | Support level provided with this plan. Possible values: - &#x60;Community&#x60;: Community support via forums and documentation - &#x60;Standard&#x60;: Standard email support with 48-hour response time - &#x60;Priority&#x60;: Priority support with 24-hour response time  | 
**monthlyPrice** | [**ListPlans200ResponsePlansValueMonthlyPrice**](ListPlans200ResponsePlansValueMonthlyPrice.md) |  | [optional] 
**annualPrice** | [**ListPlans200ResponsePlansValueAnnualPrice**](ListPlans200ResponsePlansValueAnnualPrice.md) |  | [optional] 
**discountPercentage** | **Number** | Discount percentage for annual billing | [optional] 


