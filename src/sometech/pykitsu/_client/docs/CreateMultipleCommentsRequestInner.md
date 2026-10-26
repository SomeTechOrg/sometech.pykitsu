# CreateMultipleCommentsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_status_id** | **UUID** | Task status identifier | 
**comment** | **str** | Comment text content | [optional] 
**person_id** | **UUID** | Person identifier (optional, defaults to current user) | [optional] 
**object_id** | **UUID** | Task identifier | 
**created_at** | **datetime** | Creation timestamp (optional, defaults to current time) | [optional] 
**checklist** | **object** | Checklist items for the comment | [optional] 
**links** | **List[str]** | List of related links | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_multiple_comments_request_inner import CreateMultipleCommentsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMultipleCommentsRequestInner from a JSON string
create_multiple_comments_request_inner_instance = CreateMultipleCommentsRequestInner.from_json(json)
# print the JSON string representation of the object
print(CreateMultipleCommentsRequestInner.to_json())

# convert the object into a dict
create_multiple_comments_request_inner_dict = create_multiple_comments_request_inner_instance.to_dict()
# create an instance of CreateMultipleCommentsRequestInner from a dict
create_multiple_comments_request_inner_from_dict = CreateMultipleCommentsRequestInner.from_dict(create_multiple_comments_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


