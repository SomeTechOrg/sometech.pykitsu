# CreateProductionScheduleVersionTaskLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**production_schedule_version_id** | **UUID** |  | 
**task_id** | **UUID** |  | 

## Example

```python
from sometech.pykitsu._client.models.create_production_schedule_version_task_link_request import CreateProductionScheduleVersionTaskLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductionScheduleVersionTaskLinkRequest from a JSON string
create_production_schedule_version_task_link_request_instance = CreateProductionScheduleVersionTaskLinkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProductionScheduleVersionTaskLinkRequest.to_json())

# convert the object into a dict
create_production_schedule_version_task_link_request_dict = create_production_schedule_version_task_link_request_instance.to_dict()
# create an instance of CreateProductionScheduleVersionTaskLinkRequest from a dict
create_production_schedule_version_task_link_request_from_dict = CreateProductionScheduleVersionTaskLinkRequest.from_dict(create_production_schedule_version_task_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


