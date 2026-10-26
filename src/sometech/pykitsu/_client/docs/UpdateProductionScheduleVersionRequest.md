# UpdateProductionScheduleVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_production_schedule_version_request import UpdateProductionScheduleVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductionScheduleVersionRequest from a JSON string
update_production_schedule_version_request_instance = UpdateProductionScheduleVersionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProductionScheduleVersionRequest.to_json())

# convert the object into a dict
update_production_schedule_version_request_dict = update_production_schedule_version_request_instance.to_dict()
# create an instance of UpdateProductionScheduleVersionRequest from a dict
update_production_schedule_version_request_from_dict = UpdateProductionScheduleVersionRequest.from_dict(update_production_schedule_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


