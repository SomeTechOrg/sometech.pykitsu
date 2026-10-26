# CreateStatusAutomationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_task_status_id** | **UUID** |  | 
**target_task_status_id** | **UUID** |  | 
**field_name** | **str** |  | 
**field_value** | **str** |  | 

## Example

```python
from sometech.pykitsu._client.models.create_status_automation_request import CreateStatusAutomationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStatusAutomationRequest from a JSON string
create_status_automation_request_instance = CreateStatusAutomationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateStatusAutomationRequest.to_json())

# convert the object into a dict
create_status_automation_request_dict = create_status_automation_request_instance.to_dict()
# create an instance of CreateStatusAutomationRequest from a dict
create_status_automation_request_from_dict = CreateStatusAutomationRequest.from_dict(create_status_automation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


