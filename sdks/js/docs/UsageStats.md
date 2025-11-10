# Qoery.UsageStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**userId** | **String** | User identifier | 
**plan** | **String** | Current subscription plan. Possible values: - &#x60;free&#x60;: Free tier with basic limits - &#x60;starter&#x60;: Starter plan for small projects - &#x60;pro&#x60;: Professional plan for production use - &#x60;growth&#x60;: Growth plan for large-scale operations  | 
**totalUsage** | **Number** | Total number of API calls across all endpoints | 
**totalErrors** | **Number** | Total number of errors across all endpoints | 
**endpointBreakdown** | [**[GetUsageStats200ResponseEndpointBreakdownInner]**](GetUsageStats200ResponseEndpointBreakdownInner.md) | Usage breakdown by endpoint | 



## Enum: PlanEnum


* `free` (value: `"free"`)

* `starter` (value: `"starter"`)

* `pro` (value: `"pro"`)

* `growth` (value: `"growth"`)




