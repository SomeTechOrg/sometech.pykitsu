# GetProjectAttachmentFiles200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Attachment file unique identifier | [optional] 
**name** | **str** | File name | [optional] 
**mimetype** | **str** | File MIME type | [optional] 
**size** | **int** | File size in bytes | [optional] 
**comment_id** | **UUID** | Comment identifier | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_attachment_files200_response_inner import GetProjectAttachmentFiles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectAttachmentFiles200ResponseInner from a JSON string
get_project_attachment_files200_response_inner_instance = GetProjectAttachmentFiles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectAttachmentFiles200ResponseInner.to_json())

# convert the object into a dict
get_project_attachment_files200_response_inner_dict = get_project_attachment_files200_response_inner_instance.to_dict()
# create an instance of GetProjectAttachmentFiles200ResponseInner from a dict
get_project_attachment_files200_response_inner_from_dict = GetProjectAttachmentFiles200ResponseInner.from_dict(get_project_attachment_files200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


