# SetMainPreviewFromTask200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**preview_file_id** | **UUID** |  | [optional] 
**entity_type_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_main_preview_from_task200_response import SetMainPreviewFromTask200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetMainPreviewFromTask200Response from a JSON string
set_main_preview_from_task200_response_instance = SetMainPreviewFromTask200Response.from_json(json)
# print the JSON string representation of the object
print(SetMainPreviewFromTask200Response.to_json())

# convert the object into a dict
set_main_preview_from_task200_response_dict = set_main_preview_from_task200_response_instance.to_dict()
# create an instance of SetMainPreviewFromTask200Response from a dict
set_main_preview_from_task200_response_from_dict = SetMainPreviewFromTask200Response.from_dict(set_main_preview_from_task200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


