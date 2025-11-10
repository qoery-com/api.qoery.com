# Qoery.V0UsageGet200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**userId** | **String** | User identifier | 
**plan** | **String** | Current subscription plan | 
**totalUsage** | **Number** | Total number of API calls across all endpoints | 
**totalErrors** | **Number** | Total number of errors across all endpoints | 
**endpointBreakdown** | [**[V0UsageGet200ResponseEndpointBreakdownInner]**](V0UsageGet200ResponseEndpointBreakdownInner.md) | Usage breakdown by endpoint | 



## Enum: PlanEnum


* `free` (value: `"free"`)

* `starter` (value: `"starter"`)

* `pro` (value: `"pro"`)

* `growth` (value: `"growth"`)




