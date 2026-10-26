# UpdatePluginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_plugin_request import UpdatePluginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePluginRequest from a JSON string
update_plugin_request_instance = UpdatePluginRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePluginRequest.to_json())

# convert the object into a dict
update_plugin_request_dict = update_plugin_request_instance.to_dict()
# create an instance of UpdatePluginRequest from a dict
update_plugin_request_from_dict = UpdatePluginRequest.from_dict(update_plugin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


