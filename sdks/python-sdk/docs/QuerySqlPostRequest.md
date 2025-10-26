# QuerySqlPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | SQL query to execute | 

## Example

```python
from qoery.models.query_sql_post_request import QuerySqlPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySqlPostRequest from a JSON string
query_sql_post_request_instance = QuerySqlPostRequest.from_json(json)
# print the JSON string representation of the object
print(QuerySqlPostRequest.to_json())

# convert the object into a dict
query_sql_post_request_dict = query_sql_post_request_instance.to_dict()
# create an instance of QuerySqlPostRequest from a dict
query_sql_post_request_from_dict = QuerySqlPostRequest.from_dict(query_sql_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


