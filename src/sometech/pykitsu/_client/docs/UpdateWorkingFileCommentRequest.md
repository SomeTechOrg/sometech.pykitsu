# UpdateWorkingFileCommentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Working file comment | 

## Example

```python
from sometech.pykitsu._client.models.update_working_file_comment_request import UpdateWorkingFileCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkingFileCommentRequest from a JSON string
update_working_file_comment_request_instance = UpdateWorkingFileCommentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkingFileCommentRequest.to_json())

# convert the object into a dict
update_working_file_comment_request_dict = update_working_file_comment_request_instance.to_dict()
# create an instance of UpdateWorkingFileCommentRequest from a dict
update_working_file_comment_request_from_dict = UpdateWorkingFileCommentRequest.from_dict(update_working_file_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


