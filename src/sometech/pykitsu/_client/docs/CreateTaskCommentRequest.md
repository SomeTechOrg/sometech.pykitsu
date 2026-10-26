# CreateTaskCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_status_id** | **UUID** | Task status identifier | 
**comment** | **str** | Comment text content | [optional] 
**person_id** | **UUID** | Person identifier (optional, defaults to current user) | [optional] 
**created_at** | **datetime** | Creation timestamp (optional, defaults to current time) | [optional] 
**checklist** | **object** | Checklist items for the comment | [optional] 
**links** | **List[str]** | List of related links | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_task_comment_request import CreateTaskCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskCommentRequest from a JSON string
create_task_comment_request_instance = CreateTaskCommentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTaskCommentRequest.to_json())

# convert the object into a dict
create_task_comment_request_dict = create_task_comment_request_instance.to_dict()
# create an instance of CreateTaskCommentRequest from a dict
create_task_comment_request_from_dict = CreateTaskCommentRequest.from_dict(create_task_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


