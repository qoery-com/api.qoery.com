# ScrapeGet200ResponseMetadata

Additional metadata about the scrape

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_count** | **int** | Number of observations extracted | [optional] 

## Example

```python
from qoery.models.scrape_get200_response_metadata import ScrapeGet200ResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ScrapeGet200ResponseMetadata from a JSON string
scrape_get200_response_metadata_instance = ScrapeGet200ResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(ScrapeGet200ResponseMetadata.to_json())

# convert the object into a dict
scrape_get200_response_metadata_dict = scrape_get200_response_metadata_instance.to_dict()
# create an instance of ScrapeGet200ResponseMetadata from a dict
scrape_get200_response_metadata_from_dict = ScrapeGet200ResponseMetadata.from_dict(scrape_get200_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


