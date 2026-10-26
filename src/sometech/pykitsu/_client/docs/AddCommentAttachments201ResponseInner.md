# AddCommentAttachments201ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Attachment file unique identifier | [optional] 
**name** | **str** | File name | [optional] 
**mimetype** | **str** | File MIME type | [optional] 
**size** | **int** | File size in bytes | [optional] 
**comment_id** | **UUID** | Comment identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.add_comment_attachments201_response_inner import AddCommentAttachments201ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AddCommentAttachments201ResponseInner from a JSON string
add_comment_attachments201_response_inner_instance = AddCommentAttachments201ResponseInner.from_json(json)
# print the JSON string representation of the object
print(AddCommentAttachments201ResponseInner.to_json())

# convert the object into a dict
add_comment_attachments201_response_inner_dict = add_comment_attachments201_response_inner_instance.to_dict()
# create an instance of AddCommentAttachments201ResponseInner from a dict
add_comment_attachments201_response_inner_from_dict = AddCommentAttachments201ResponseInner.from_dict(add_comment_attachments201_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


