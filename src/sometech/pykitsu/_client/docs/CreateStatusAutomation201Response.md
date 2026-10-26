# CreateStatusAutomation201Response


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
from sometech.pykitsu._client.models.create_status_automation201_response import CreateStatusAutomation201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStatusAutomation201Response from a JSON string
create_status_automation201_response_instance = CreateStatusAutomation201Response.from_json(json)
# print the JSON string representation of the object
print(CreateStatusAutomation201Response.to_json())

# convert the object into a dict
create_status_automation201_response_dict = create_status_automation201_response_instance.to_dict()
# create an instance of CreateStatusAutomation201Response from a dict
create_status_automation201_response_from_dict = CreateStatusAutomation201Response.from_dict(create_status_automation201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


