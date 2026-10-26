# UpdateStatusAutomation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**source_task_status_id** | **UUID** |  | [optional] 
**target_task_status_id** | **UUID** |  | [optional] 
**field_name** | **str** |  | [optional] 
**field_value** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_status_automation200_response import UpdateStatusAutomation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStatusAutomation200Response from a JSON string
update_status_automation200_response_instance = UpdateStatusAutomation200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateStatusAutomation200Response.to_json())

# convert the object into a dict
update_status_automation200_response_dict = update_status_automation200_response_instance.to_dict()
# create an instance of UpdateStatusAutomation200Response from a dict
update_status_automation200_response_from_dict = UpdateStatusAutomation200Response.from_dict(update_status_automation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


