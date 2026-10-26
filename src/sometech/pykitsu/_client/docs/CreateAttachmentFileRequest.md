# CreateAttachmentFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**comment_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_attachment_file_request import CreateAttachmentFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAttachmentFileRequest from a JSON string
create_attachment_file_request_instance = CreateAttachmentFileRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAttachmentFileRequest.to_json())

# convert the object into a dict
create_attachment_file_request_dict = create_attachment_file_request_instance.to_dict()
# create an instance of CreateAttachmentFileRequest from a dict
create_attachment_file_request_from_dict = CreateAttachmentFileRequest.from_dict(create_attachment_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


