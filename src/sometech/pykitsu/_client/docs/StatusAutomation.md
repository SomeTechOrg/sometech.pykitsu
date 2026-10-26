# StatusAutomation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** |  | [optional] [default to 'asset']
**in_task_type_id** | **UUID** | Task type ID | [optional] 
**in_task_status_id** | **UUID** | Task status ID | [optional] 
**out_field_type** | **str** | Field type (status, ready_for) | [optional] 
**out_task_type_id** | **UUID** | Task type ID | [optional] 
**out_task_status_id** | **UUID** | Task status ID | [optional] 

## Example

```python
from sometech.pykitsu._client.models.status_automation import StatusAutomation

# TODO update the JSON string below
json = "{}"
# create an instance of StatusAutomation from a JSON string
status_automation_instance = StatusAutomation.from_json(json)
# print the JSON string representation of the object
print(StatusAutomation.to_json())

# convert the object into a dict
status_automation_dict = status_automation_instance.to_dict()
# create an instance of StatusAutomation from a dict
status_automation_from_dict = StatusAutomation.from_dict(status_automation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


