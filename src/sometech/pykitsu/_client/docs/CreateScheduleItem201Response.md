# CreateScheduleItem201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 
**object_id** | **UUID** |  | [optional] 
**man_days** | **float** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_schedule_item201_response import CreateScheduleItem201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleItem201Response from a JSON string
create_schedule_item201_response_instance = CreateScheduleItem201Response.from_json(json)
# print the JSON string representation of the object
print(CreateScheduleItem201Response.to_json())

# convert the object into a dict
create_schedule_item201_response_dict = create_schedule_item201_response_instance.to_dict()
# create an instance of CreateScheduleItem201Response from a dict
create_schedule_item201_response_from_dict = CreateScheduleItem201Response.from_dict(create_schedule_item201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


