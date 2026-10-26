# GetCommentGetDataTasksTaskIdCommentsCommentId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**object_id** | **UUID** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**text** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_comment_get_data_tasks_task_id_comments_comment_id200_response import GetCommentGetDataTasksTaskIdCommentsCommentId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCommentGetDataTasksTaskIdCommentsCommentId200Response from a JSON string
get_comment_get_data_tasks_task_id_comments_comment_id200_response_instance = GetCommentGetDataTasksTaskIdCommentsCommentId200Response.from_json(json)
# print the JSON string representation of the object
print(GetCommentGetDataTasksTaskIdCommentsCommentId200Response.to_json())

# convert the object into a dict
get_comment_get_data_tasks_task_id_comments_comment_id200_response_dict = get_comment_get_data_tasks_task_id_comments_comment_id200_response_instance.to_dict()
# create an instance of GetCommentGetDataTasksTaskIdCommentsCommentId200Response from a dict
get_comment_get_data_tasks_task_id_comments_comment_id200_response_from_dict = GetCommentGetDataTasksTaskIdCommentsCommentId200Response.from_dict(get_comment_get_data_tasks_task_id_comments_comment_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


