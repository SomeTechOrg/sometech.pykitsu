# UpdateWorkingFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**revision** | **int** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_working_file_request import UpdateWorkingFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkingFileRequest from a JSON string
update_working_file_request_instance = UpdateWorkingFileRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkingFileRequest.to_json())

# convert the object into a dict
update_working_file_request_dict = update_working_file_request_instance.to_dict()
# create an instance of UpdateWorkingFileRequest from a dict
update_working_file_request_from_dict = UpdateWorkingFileRequest.from_dict(update_working_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


