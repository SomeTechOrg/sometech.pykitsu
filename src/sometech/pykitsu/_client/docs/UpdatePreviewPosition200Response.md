# UpdatePreviewPosition200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Preview file unique identifier | [optional] 
**position** | **int** | Preview position | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_preview_position200_response import UpdatePreviewPosition200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePreviewPosition200Response from a JSON string
update_preview_position200_response_instance = UpdatePreviewPosition200Response.from_json(json)
# print the JSON string representation of the object
print(UpdatePreviewPosition200Response.to_json())

# convert the object into a dict
update_preview_position200_response_dict = update_preview_position200_response_instance.to_dict()
# create an instance of UpdatePreviewPosition200Response from a dict
update_preview_position200_response_from_dict = UpdatePreviewPosition200Response.from_dict(update_preview_position200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


