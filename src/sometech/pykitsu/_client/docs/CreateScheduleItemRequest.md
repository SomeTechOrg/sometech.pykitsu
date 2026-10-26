# CreateScheduleItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **UUID** |  | 
**task_type_id** | **UUID** |  | 
**object_id** | **UUID** |  | 
**man_days** | **float** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_schedule_item_request import CreateScheduleItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleItemRequest from a JSON string
create_schedule_item_request_instance = CreateScheduleItemRequest.from_json(json)
# print the JSON string representation of the object
print(CreateScheduleItemRequest.to_json())

# convert the object into a dict
create_schedule_item_request_dict = create_schedule_item_request_instance.to_dict()
# create an instance of CreateScheduleItemRequest from a dict
create_schedule_item_request_from_dict = CreateScheduleItemRequest.from_dict(create_schedule_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


