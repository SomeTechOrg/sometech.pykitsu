# GetProductionScheduleVersionTaskLink200Response


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
from sometech.pykitsu._client.models.get_production_schedule_version_task_link200_response import GetProductionScheduleVersionTaskLink200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductionScheduleVersionTaskLink200Response from a JSON string
get_production_schedule_version_task_link200_response_instance = GetProductionScheduleVersionTaskLink200Response.from_json(json)
# print the JSON string representation of the object
print(GetProductionScheduleVersionTaskLink200Response.to_json())

# convert the object into a dict
get_production_schedule_version_task_link200_response_dict = get_production_schedule_version_task_link200_response_instance.to_dict()
# create an instance of GetProductionScheduleVersionTaskLink200Response from a dict
get_production_schedule_version_task_link200_response_from_dict = GetProductionScheduleVersionTaskLink200Response.from_dict(get_production_schedule_version_task_link200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


