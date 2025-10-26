# SQLQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | SQL query to execute | 

## Example

```python
from qoery.models.sql_query_request import SQLQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SQLQueryRequest from a JSON string
sql_query_request_instance = SQLQueryRequest.from_json(json)
# print the JSON string representation of the object
print(SQLQueryRequest.to_json())

# convert the object into a dict
sql_query_request_dict = sql_query_request_instance.to_dict()
# create an instance of SQLQueryRequest from a dict
sql_query_request_from_dict = SQLQueryRequest.from_dict(sql_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


