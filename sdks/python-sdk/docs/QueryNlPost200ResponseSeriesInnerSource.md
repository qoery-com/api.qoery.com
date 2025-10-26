# QueryNlPost200ResponseSeriesInnerSource

Provenance record for a dataset or observation source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Numeric ID of the source in the database | 
**url** | **str** | Canonical URL of the data source | 
**description** | **str** | Human-readable description of the source | [optional] 

## Example

```python
from qoery.models.query_nl_post200_response_series_inner_source import QueryNlPost200ResponseSeriesInnerSource

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNlPost200ResponseSeriesInnerSource from a JSON string
query_nl_post200_response_series_inner_source_instance = QueryNlPost200ResponseSeriesInnerSource.from_json(json)
# print the JSON string representation of the object
print(QueryNlPost200ResponseSeriesInnerSource.to_json())

# convert the object into a dict
query_nl_post200_response_series_inner_source_dict = query_nl_post200_response_series_inner_source_instance.to_dict()
# create an instance of QueryNlPost200ResponseSeriesInnerSource from a dict
query_nl_post200_response_series_inner_source_from_dict = QueryNlPost200ResponseSeriesInnerSource.from_dict(query_nl_post200_response_series_inner_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


