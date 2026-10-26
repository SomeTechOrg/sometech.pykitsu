# AddStatusAutomationToProductionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_automation_id** | **UUID** | Status automation unique identifier | 

## Example

```python
from sometech.pykitsu._client.models.add_status_automation_to_production_request import AddStatusAutomationToProductionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddStatusAutomationToProductionRequest from a JSON string
add_status_automation_to_production_request_instance = AddStatusAutomationToProductionRequest.from_json(json)
# print the JSON string representation of the object
print(AddStatusAutomationToProductionRequest.to_json())

# convert the object into a dict
add_status_automation_to_production_request_dict = add_status_automation_to_production_request_instance.to_dict()
# create an instance of AddStatusAutomationToProductionRequest from a dict
add_status_automation_to_production_request_from_dict = AddStatusAutomationToProductionRequest.from_dict(add_status_automation_to_production_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


