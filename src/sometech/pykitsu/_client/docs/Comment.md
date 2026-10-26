# Comment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 
**object_id** | **UUID** | Unique ID of the commented model instance | [optional] 
**object_type** | **str** | Model type of the comment model instance | [optional] 
**text** | **str** |  | [optional] 
**data** | **str** | Free JSON field to add metadata | [optional] 
**replies** | **str** |  | [optional] [default to '[]']
**checklist** | **str** |  | [optional] 
**pinned** | **bool** |  | [optional] 
**task_status_id** | **UUID** | Task status attached to comment | [optional] 
**person_id** | **UUID** | The person who publishes the comment | [optional] 
**preview_file_id** | **UUID** | ID of preview file used as thumbnail | [optional] 
**id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_from_dict = Comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


