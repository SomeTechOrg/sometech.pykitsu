# UpdatePreviewAnnotationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **List[object]** | Annotations to add | [optional] 
**updates** | **List[object]** | Annotations to update | [optional] 
**deletions** | **List[UUID]** | Annotation IDs to remove | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_preview_annotations_request import UpdatePreviewAnnotationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePreviewAnnotationsRequest from a JSON string
update_preview_annotations_request_instance = UpdatePreviewAnnotationsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePreviewAnnotationsRequest.to_json())

# convert the object into a dict
update_preview_annotations_request_dict = update_preview_annotations_request_instance.to_dict()
# create an instance of UpdatePreviewAnnotationsRequest from a dict
update_preview_annotations_request_from_dict = UpdatePreviewAnnotationsRequest.from_dict(update_preview_annotations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


