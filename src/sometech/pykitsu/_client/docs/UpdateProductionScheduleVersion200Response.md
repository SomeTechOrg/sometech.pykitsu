# UpdateProductionScheduleVersion200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_production_schedule_version200_response import UpdateProductionScheduleVersion200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductionScheduleVersion200Response from a JSON string
update_production_schedule_version200_response_instance = UpdateProductionScheduleVersion200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateProductionScheduleVersion200Response.to_json())

# convert the object into a dict
update_production_schedule_version200_response_dict = update_production_schedule_version200_response_instance.to_dict()
# create an instance of UpdateProductionScheduleVersion200Response from a dict
update_production_schedule_version200_response_from_dict = UpdateProductionScheduleVersion200Response.from_dict(update_production_schedule_version200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


