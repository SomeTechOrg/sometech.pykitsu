# UpdatePreviewAnnotations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Preview file unique identifier | [optional] 
**annotations** | **List[object]** | Updated annotations | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_preview_annotations200_response import UpdatePreviewAnnotations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePreviewAnnotations200Response from a JSON string
update_preview_annotations200_response_instance = UpdatePreviewAnnotations200Response.from_json(json)
# print the JSON string representation of the object
print(UpdatePreviewAnnotations200Response.to_json())

# convert the object into a dict
update_preview_annotations200_response_dict = update_preview_annotations200_response_instance.to_dict()
# create an instance of UpdatePreviewAnnotations200Response from a dict
update_preview_annotations200_response_from_dict = UpdatePreviewAnnotations200Response.from_dict(update_preview_annotations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


