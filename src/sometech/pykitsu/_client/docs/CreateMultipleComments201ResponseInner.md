# CreateMultipleComments201ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Comment unique identifier | [optional] 
**task_id** | **UUID** | Task identifier | [optional] 
**person_id** | **UUID** | Person identifier | [optional] 
**comment** | **str** | Comment text content | [optional] 
**task_status_id** | **UUID** | Task status identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_multiple_comments201_response_inner import CreateMultipleComments201ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMultipleComments201ResponseInner from a JSON string
create_multiple_comments201_response_inner_instance = CreateMultipleComments201ResponseInner.from_json(json)
# print the JSON string representation of the object
print(CreateMultipleComments201ResponseInner.to_json())

# convert the object into a dict
create_multiple_comments201_response_inner_dict = create_multiple_comments201_response_inner_instance.to_dict()
# create an instance of CreateMultipleComments201ResponseInner from a dict
create_multiple_comments201_response_inner_from_dict = CreateMultipleComments201ResponseInner.from_dict(create_multiple_comments201_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


