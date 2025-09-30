# Qoery.ScrapeGet200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | **String** | Original HTML of the page (if requested) | [optional] 
**markdown** | **String** | Markdown representation of the page (if requested) | [optional] 
**series** | [**[ScrapeGet200ResponseSeriesInner]**](ScrapeGet200ResponseSeriesInner.md) | Extracted time series from detected tables (fresh scrape) or structured DB series (cached) | 
**artifacts** | [**ScrapeGet200ResponseArtifacts**](ScrapeGet200ResponseArtifacts.md) |  | [optional] 
**cached** | **Boolean** | Whether this result was retrieved from cache | [optional] 
**sourceId** | **Number** | Database source ID (present when cached&#x3D;true) | [optional] 


