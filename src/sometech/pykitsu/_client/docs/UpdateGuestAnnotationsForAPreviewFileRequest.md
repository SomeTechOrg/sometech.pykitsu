# UpdateGuestAnnotationsForAPreviewFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **UUID** |  | 
**preview_file_id** | **UUID** |  | 
**additions** | **List[object]** |  | [optional] 
**updates** | **List[object]** |  | [optional] 
**deletions** | **List[UUID]** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_guest_annotations_for_a_preview_file_request import UpdateGuestAnnotationsForAPreviewFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGuestAnnotationsForAPreviewFileRequest from a JSON string
update_guest_annotations_for_a_preview_file_request_instance = UpdateGuestAnnotationsForAPreviewFileRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGuestAnnotationsForAPreviewFileRequest.to_json())

# convert the object into a dict
update_guest_annotations_for_a_preview_file_request_dict = update_guest_annotations_for_a_preview_file_request_instance.to_dict()
# create an instance of UpdateGuestAnnotationsForAPreviewFileRequest from a dict
update_guest_annotations_for_a_preview_file_request_from_dict = UpdateGuestAnnotationsForAPreviewFileRequest.from_dict(update_guest_annotations_for_a_preview_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


