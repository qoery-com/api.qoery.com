# ScrapePost200ResponseArtifacts

URLs to stored artifacts for larger payloads

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_url** | **str** |  | [optional] 
**markdown_url** | **str** |  | [optional] 
**tables_base_url** | **str** |  | [optional] 

## Example

```python
from qoery.models.scrape_post200_response_artifacts import ScrapePost200ResponseArtifacts

# TODO update the JSON string below
json = "{}"
# create an instance of ScrapePost200ResponseArtifacts from a JSON string
scrape_post200_response_artifacts_instance = ScrapePost200ResponseArtifacts.from_json(json)
# print the JSON string representation of the object
print(ScrapePost200ResponseArtifacts.to_json())

# convert the object into a dict
scrape_post200_response_artifacts_dict = scrape_post200_response_artifacts_instance.to_dict()
# create an instance of ScrapePost200ResponseArtifacts from a dict
scrape_post200_response_artifacts_from_dict = ScrapePost200ResponseArtifacts.from_dict(scrape_post200_response_artifacts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


