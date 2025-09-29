# URLRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from qoery.models.url_request import URLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of URLRequest from a JSON string
url_request_instance = URLRequest.from_json(json)
# print the JSON string representation of the object
print(URLRequest.to_json())

# convert the object into a dict
url_request_dict = url_request_instance.to_dict()
# create an instance of URLRequest from a dict
url_request_from_dict = URLRequest.from_dict(url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


