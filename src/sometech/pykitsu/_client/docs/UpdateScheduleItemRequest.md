# UpdateScheduleItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**man_days** | **float** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_schedule_item_request import UpdateScheduleItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleItemRequest from a JSON string
update_schedule_item_request_instance = UpdateScheduleItemRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleItemRequest.to_json())

# convert the object into a dict
update_schedule_item_request_dict = update_schedule_item_request_instance.to_dict()
# create an instance of UpdateScheduleItemRequest from a dict
update_schedule_item_request_from_dict = UpdateScheduleItemRequest.from_dict(update_schedule_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


