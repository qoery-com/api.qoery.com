# Series


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_id** | **str** | short id for the series (optional but recommended) | [optional] 
**name** | **str** | human-friendly name for the series | 
**unit** | **str** | unit of measurement (optional) | [optional] 
**observations** | [**List[QueryNlPost200ResponseAllOfSeriesInnerObservationsInner]**](QueryNlPost200ResponseAllOfSeriesInnerObservationsInner.md) |  | 

## Example

```python
from qoery.models.series import Series

# TODO update the JSON string below
json = "{}"
# create an instance of Series from a JSON string
series_instance = Series.from_json(json)
# print the JSON string representation of the object
print(Series.to_json())

# convert the object into a dict
series_dict = series_instance.to_dict()
# create an instance of Series from a dict
series_from_dict = Series.from_dict(series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


