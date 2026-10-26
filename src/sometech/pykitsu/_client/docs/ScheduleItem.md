# ScheduleItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**man_days** | **int** |  | [optional] 
**project_id** | **UUID** | Project ID | [optional] 
**task_type_id** | **UUID** | Task type ID | [optional] 
**object_id** | **UUID** | Object ID | [optional] 

## Example

```python
from sometech.pykitsu._client.models.schedule_item import ScheduleItem

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleItem from a JSON string
schedule_item_instance = ScheduleItem.from_json(json)
# print the JSON string representation of the object
print(ScheduleItem.to_json())

# convert the object into a dict
schedule_item_dict = schedule_item_instance.to_dict()
# create an instance of ScheduleItem from a dict
schedule_item_from_dict = ScheduleItem.from_dict(schedule_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


