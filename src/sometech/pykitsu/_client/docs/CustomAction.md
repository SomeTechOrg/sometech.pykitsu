# CustomAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of custom action | [optional] 
**url** | **str** |  | [optional] 
**entity_type** | **str** |  | [optional] [default to 'all']
**is_ajax** | **bool** | True if the custom action is ajax, False otherwise | [optional] [default to False]

## Example

```python
from sometech.pykitsu._client.models.custom_action import CustomAction

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAction from a JSON string
custom_action_instance = CustomAction.from_json(json)
# print the JSON string representation of the object
print(CustomAction.to_json())

# convert the object into a dict
custom_action_dict = custom_action_instance.to_dict()
# create an instance of CustomAction from a dict
custom_action_from_dict = CustomAction.from_dict(custom_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


