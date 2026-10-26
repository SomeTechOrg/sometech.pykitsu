# CreateAttachmentFile201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**comment_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_attachment_file201_response import CreateAttachmentFile201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAttachmentFile201Response from a JSON string
create_attachment_file201_response_instance = CreateAttachmentFile201Response.from_json(json)
# print the JSON string representation of the object
print(CreateAttachmentFile201Response.to_json())

# convert the object into a dict
create_attachment_file201_response_dict = create_attachment_file201_response_instance.to_dict()
# create an instance of CreateAttachmentFile201Response from a dict
create_attachment_file201_response_from_dict = CreateAttachmentFile201Response.from_dict(create_attachment_file201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


