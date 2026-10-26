# UpdateStatusAutomationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**field_value** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_status_automation_request import UpdateStatusAutomationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStatusAutomationRequest from a JSON string
update_status_automation_request_instance = UpdateStatusAutomationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateStatusAutomationRequest.to_json())

# convert the object into a dict
update_status_automation_request_dict = update_status_automation_request_instance.to_dict()
# create an instance of UpdateStatusAutomationRequest from a dict
update_status_automation_request_from_dict = UpdateStatusAutomationRequest.from_dict(update_status_automation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


