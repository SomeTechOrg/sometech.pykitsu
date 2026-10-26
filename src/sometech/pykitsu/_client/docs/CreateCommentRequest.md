# CreateCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **UUID** |  | 
**person_id** | **UUID** |  | 
**task_status_id** | **UUID** |  | 
**text** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_comment_request import CreateCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommentRequest from a JSON string
create_comment_request_instance = CreateCommentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCommentRequest.to_json())

# convert the object into a dict
create_comment_request_dict = create_comment_request_instance.to_dict()
# create an instance of CreateCommentRequest from a dict
create_comment_request_from_dict = CreateCommentRequest.from_dict(create_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


