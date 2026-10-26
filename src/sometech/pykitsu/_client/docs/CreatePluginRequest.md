# CreatePluginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**active** | **bool** |  | [optional] [default to False]

## Example

```python
from sometech.pykitsu._client.models.create_plugin_request import CreatePluginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePluginRequest from a JSON string
create_plugin_request_instance = CreatePluginRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePluginRequest.to_json())

# convert the object into a dict
create_plugin_request_dict = create_plugin_request_instance.to_dict()
# create an instance of CreatePluginRequest from a dict
create_plugin_request_from_dict = CreatePluginRequest.from_dict(create_plugin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


