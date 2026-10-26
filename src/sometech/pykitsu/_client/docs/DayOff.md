# DayOff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**person_id** | **UUID** | The person who will take the day off | [optional] 

## Example

```python
from sometech.pykitsu._client.models.day_off import DayOff

# TODO update the JSON string below
json = "{}"
# create an instance of DayOff from a JSON string
day_off_instance = DayOff.from_json(json)
# print the JSON string representation of the object
print(DayOff.to_json())

# convert the object into a dict
day_off_dict = day_off_instance.to_dict()
# create an instance of DayOff from a dict
day_off_from_dict = DayOff.from_dict(day_off_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


