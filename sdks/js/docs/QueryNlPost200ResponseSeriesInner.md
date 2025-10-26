# Qoery.QueryNlPost200ResponseSeriesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | ID of the series | [optional] 
**name** | **String** | Human-readable name of the series | [optional] 
**entity** | [**QueryNlPost200ResponseSeriesInnerEntity**](QueryNlPost200ResponseSeriesInnerEntity.md) |  | 
**metric** | [**QueryNlPost200ResponseSeriesInnerMetric**](QueryNlPost200ResponseSeriesInnerMetric.md) |  | 
**unit** | [**QueryNlPost200ResponseSeriesInnerUnit**](QueryNlPost200ResponseSeriesInnerUnit.md) |  | [optional] 
**source** | [**QueryNlPost200ResponseSeriesInnerSource**](QueryNlPost200ResponseSeriesInnerSource.md) |  | 
**frequency** | **String** | Frequency of the time series (e.g., monthly, annual) | [optional] 
**description** | **String** | Description of the series | [optional] 
**labels** | **{String: Object}** | Additional labels and metadata at the series level | [optional] 
**observations** | [**[QueryNlPost200ResponseSeriesInnerObservationsInner]**](QueryNlPost200ResponseSeriesInnerObservationsInner.md) | The ordered observations for this series | 


