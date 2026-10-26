# SetTaskLinksFromProductionScheduleVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**production_schedule_version_id** | **UUID** | Source production schedule version unique identifier | 

## Example

```python
from sometech.pykitsu._client.models.set_task_links_from_production_schedule_version_request import SetTaskLinksFromProductionScheduleVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTaskLinksFromProductionScheduleVersionRequest from a JSON string
set_task_links_from_production_schedule_version_request_instance = SetTaskLinksFromProductionScheduleVersionRequest.from_json(json)
# print the JSON string representation of the object
print(SetTaskLinksFromProductionScheduleVersionRequest.to_json())

# convert the object into a dict
set_task_links_from_production_schedule_version_request_dict = set_task_links_from_production_schedule_version_request_instance.to_dict()
# create an instance of SetTaskLinksFromProductionScheduleVersionRequest from a dict
set_task_links_from_production_schedule_version_request_from_dict = SetTaskLinksFromProductionScheduleVersionRequest.from_dict(set_task_links_from_production_schedule_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


