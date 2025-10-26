# Qoery.ScrapeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**[QueryNlGet200ResponseSeriesInner]**](QueryNlGet200ResponseSeriesInner.md) | Array of series with observations (same structure as query endpoints) | 
**artifacts** | [**ScrapeGet200ResponseArtifacts**](ScrapeGet200ResponseArtifacts.md) |  | [optional] 
**cached** | **Boolean** | Whether this result was retrieved from cache | [optional] 
**sourceId** | **String** | Database source ID (present when cached&#x3D;true) | [optional] 
**metadata** | [**ScrapeGet200ResponseMetadata**](ScrapeGet200ResponseMetadata.md) |  | [optional] 
**html** | **String** | Original HTML of the page (only if html&#x3D;true query param) | [optional] 
**markdown** | **String** | Markdown representation of the page (only if markdown&#x3D;true query param) | [optional] 


