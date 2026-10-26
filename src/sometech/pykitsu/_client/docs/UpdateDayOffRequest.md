# UpdateDayOffRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_day_off_request import UpdateDayOffRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDayOffRequest from a JSON string
update_day_off_request_instance = UpdateDayOffRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDayOffRequest.to_json())

# convert the object into a dict
update_day_off_request_dict = update_day_off_request_instance.to_dict()
# create an instance of UpdateDayOffRequest from a dict
update_day_off_request_from_dict = UpdateDayOffRequest.from_dict(update_day_off_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


