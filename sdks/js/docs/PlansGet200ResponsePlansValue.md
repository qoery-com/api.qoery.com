# Qoery.PlansGet200ResponsePlansValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**price** | **String** | Human-friendly display price | [optional] 
**billing** | **String** | Billing cadence for display (e.g., monthly, annual, one-time) | [optional] 
**limits** | **{String: Number}** | Monthly limits keyed by endpoint (e.g., &#39;query/nl&#39;, &#39;scrape&#39;, &#39;plot2table&#39;) | [optional] 
**apiKeys** | [**PlansGet200ResponsePlansValueApiKeys**](PlansGet200ResponsePlansValueApiKeys.md) |  | [optional] 
**support** | **String** |  | [optional] 
**monthlyPrice** | [**PlansGet200ResponsePlansValueMonthlyPrice**](PlansGet200ResponsePlansValueMonthlyPrice.md) |  | [optional] 
**annualPrice** | [**PlansGet200ResponsePlansValueMonthlyPrice**](PlansGet200ResponsePlansValueMonthlyPrice.md) |  | [optional] 
**discountPercentage** | **Number** |  | [optional] 


