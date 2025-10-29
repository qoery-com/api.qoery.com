# ScrapeGet200Response

Response from web scraping endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**List[QueryNlGet200ResponseSeriesInner]**](QueryNlGet200ResponseSeriesInner.md) | Array of series with observations (same structure as query endpoints) | 
**artifacts** | [**ScrapeGet200ResponseArtifacts**](ScrapeGet200ResponseArtifacts.md) |  | [optional] 
**cached** | **bool** | Whether this result was retrieved from cache | [optional] 
**source_id** | **str** | Database source ID (present when cached&#x3D;true) | [optional] 
**metadata** | [**ScrapeGet200ResponseMetadata**](ScrapeGet200ResponseMetadata.md) |  | [optional] 

## Example

```python
from qoery.models.scrape_get200_response import ScrapeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ScrapeGet200Response from a JSON string
scrape_get200_response_instance = ScrapeGet200Response.from_json(json)
# print the JSON string representation of the object
print(ScrapeGet200Response.to_json())

# convert the object into a dict
scrape_get200_response_dict = scrape_get200_response_instance.to_dict()
# create an instance of ScrapeGet200Response from a dict
scrape_get200_response_from_dict = ScrapeGet200Response.from_dict(scrape_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


