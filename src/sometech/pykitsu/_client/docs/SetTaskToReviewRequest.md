# SetTaskToReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_id** | **UUID** |  | [optional] 
**comment** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**revision** | **int** |  | [optional] 
**change_status** | **bool** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_task_to_review_request import SetTaskToReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTaskToReviewRequest from a JSON string
set_task_to_review_request_instance = SetTaskToReviewRequest.from_json(json)
# print the JSON string representation of the object
print(SetTaskToReviewRequest.to_json())

# convert the object into a dict
set_task_to_review_request_dict = set_task_to_review_request_instance.to_dict()
# create an instance of SetTaskToReviewRequest from a dict
set_task_to_review_request_from_dict = SetTaskToReviewRequest.from_dict(set_task_to_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


