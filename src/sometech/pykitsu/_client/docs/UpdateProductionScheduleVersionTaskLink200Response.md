# UpdateProductionScheduleVersionTaskLink200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**production_schedule_version_id** | **UUID** |  | [optional] 
**task_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_production_schedule_version_task_link200_response import UpdateProductionScheduleVersionTaskLink200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductionScheduleVersionTaskLink200Response from a JSON string
update_production_schedule_version_task_link200_response_instance = UpdateProductionScheduleVersionTaskLink200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateProductionScheduleVersionTaskLink200Response.to_json())

# convert the object into a dict
update_production_schedule_version_task_link200_response_dict = update_production_schedule_version_task_link200_response_instance.to_dict()
# create an instance of UpdateProductionScheduleVersionTaskLink200Response from a dict
update_production_schedule_version_task_link200_response_from_dict = UpdateProductionScheduleVersionTaskLink200Response.from_dict(update_production_schedule_version_task_link200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


