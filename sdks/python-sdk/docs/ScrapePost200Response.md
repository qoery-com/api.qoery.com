# ScrapePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | **str** | Original HTML of the page | [optional] 
**markdown** | **str** | Markdown representation of the page | [optional] 
**series** | [**List[QueryNlPost200ResponseAllOfSeriesInner]**](QueryNlPost200ResponseAllOfSeriesInner.md) | Extracted time series from detected tables | 
**artifacts** | [**ScrapePost200ResponseArtifacts**](ScrapePost200ResponseArtifacts.md) |  | [optional] 

## Example

```python
from qoery.models.scrape_post200_response import ScrapePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ScrapePost200Response from a JSON string
scrape_post200_response_instance = ScrapePost200Response.from_json(json)
# print the JSON string representation of the object
print(ScrapePost200Response.to_json())

# convert the object into a dict
scrape_post200_response_dict = scrape_post200_response_instance.to_dict()
# create an instance of ScrapePost200Response from a dict
scrape_post200_response_from_dict = ScrapePost200Response.from_dict(scrape_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


