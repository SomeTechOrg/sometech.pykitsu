# CreateProductionScheduleVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**project_id** | **UUID** |  | 

## Example

```python
from sometech.pykitsu._client.models.create_production_schedule_version_request import CreateProductionScheduleVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductionScheduleVersionRequest from a JSON string
create_production_schedule_version_request_instance = CreateProductionScheduleVersionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProductionScheduleVersionRequest.to_json())

# convert the object into a dict
create_production_schedule_version_request_dict = create_production_schedule_version_request_instance.to_dict()
# create an instance of CreateProductionScheduleVersionRequest from a dict
create_production_schedule_version_request_from_dict = CreateProductionScheduleVersionRequest.from_dict(create_production_schedule_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


