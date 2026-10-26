# CreateWorkingFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**task_id** | **UUID** |  | 
**entity_id** | **UUID** |  | 
**revision** | **int** |  | [optional] [default to 1]

## Example

```python
from sometech.pykitsu._client.models.create_working_file_request import CreateWorkingFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWorkingFileRequest from a JSON string
create_working_file_request_instance = CreateWorkingFileRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWorkingFileRequest.to_json())

# convert the object into a dict
create_working_file_request_dict = create_working_file_request_instance.to_dict()
# create an instance of CreateWorkingFileRequest from a dict
create_working_file_request_from_dict = CreateWorkingFileRequest.from_dict(create_working_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


