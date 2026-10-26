# UpdateCustomActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url_pattern** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_custom_action_request import UpdateCustomActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomActionRequest from a JSON string
update_custom_action_request_instance = UpdateCustomActionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomActionRequest.to_json())

# convert the object into a dict
update_custom_action_request_dict = update_custom_action_request_instance.to_dict()
# create an instance of UpdateCustomActionRequest from a dict
update_custom_action_request_from_dict = UpdateCustomActionRequest.from_dict(update_custom_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


