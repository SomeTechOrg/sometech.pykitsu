# CreateCustomActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**url_pattern** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_custom_action_request import CreateCustomActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomActionRequest from a JSON string
create_custom_action_request_instance = CreateCustomActionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomActionRequest.to_json())

# convert the object into a dict
create_custom_action_request_dict = create_custom_action_request_instance.to_dict()
# create an instance of CreateCustomActionRequest from a dict
create_custom_action_request_from_dict = CreateCustomActionRequest.from_dict(create_custom_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


