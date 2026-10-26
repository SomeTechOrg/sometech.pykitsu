# CreateNewWorkingFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Working file name | 
**mode** | **str** | Working file mode | [optional] [default to 'working']
**description** | **str** | Working file description | [optional] 
**comment** | **str** | Working file comment | [optional] 
**person_id** | **UUID** | Person identifier | [optional] 
**software_id** | **UUID** | Software identifier | [optional] 
**revision** | **int** | Working file revision | [optional] 
**sep** | **str** | Path separator | [optional] [default to '/']

## Example

```python
from sometech.pykitsu._client.models.create_new_working_file_request import CreateNewWorkingFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewWorkingFileRequest from a JSON string
create_new_working_file_request_instance = CreateNewWorkingFileRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNewWorkingFileRequest.to_json())

# convert the object into a dict
create_new_working_file_request_dict = create_new_working_file_request_instance.to_dict()
# create an instance of CreateNewWorkingFileRequest from a dict
create_new_working_file_request_from_dict = CreateNewWorkingFileRequest.from_dict(create_new_working_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


