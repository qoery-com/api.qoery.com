# Qoery.ScrapePost200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**[QueryNlPost200ResponseSeriesInner]**](QueryNlPost200ResponseSeriesInner.md) | Array of observations extracted from the page (flat structure) | 
**artifacts** | [**ScrapePost200ResponseArtifacts**](ScrapePost200ResponseArtifacts.md) |  | [optional] 
**cached** | **Boolean** | Whether this result was retrieved from cache | [optional] 
**sourceId** | **String** | Database source ID (present when cached&#x3D;true) | [optional] 
**metadata** | [**ScrapePost200ResponseMetadata**](ScrapePost200ResponseMetadata.md) |  | [optional] 
**html** | **String** | Original HTML of the page (only if html&#x3D;true query param) | [optional] 
**markdown** | **String** | Markdown representation of the page (only if markdown&#x3D;true query param) | [optional] 


