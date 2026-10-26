# AttachmentFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of attachment file | [optional] 
**size** | **int** | Size of attachment file | [optional] 
**extension** | **str** | Extension of attachment file | [optional] 
**mimetype** | **str** |  | [optional] 
**comment_id** | **UUID** | Comment to which the file is attached | [optional] 
**id** | **UUID** | Attachment file unique identifier | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.attachment_file import AttachmentFile

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentFile from a JSON string
attachment_file_instance = AttachmentFile.from_json(json)
# print the JSON string representation of the object
print(AttachmentFile.to_json())

# convert the object into a dict
attachment_file_dict = attachment_file_instance.to_dict()
# create an instance of AttachmentFile from a dict
attachment_file_from_dict = AttachmentFile.from_dict(attachment_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


