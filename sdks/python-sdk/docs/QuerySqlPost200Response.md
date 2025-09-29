# QuerySqlPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**List[QueryNlPost200ResponseAllOfSeriesInner]**](QueryNlPost200ResponseAllOfSeriesInner.md) |  | 

## Example

```python
from qoery.models.query_sql_post200_response import QuerySqlPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySqlPost200Response from a JSON string
query_sql_post200_response_instance = QuerySqlPost200Response.from_json(json)
# print the JSON string representation of the object
print(QuerySqlPost200Response.to_json())

# convert the object into a dict
query_sql_post200_response_dict = query_sql_post200_response_instance.to_dict()
# create an instance of QuerySqlPost200Response from a dict
query_sql_post200_response_from_dict = QuerySqlPost200Response.from_dict(query_sql_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


