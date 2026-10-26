# CreateNewEntityOutputFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Output file name | [optional] 
**mode** | **str** | Output file mode | [optional] [default to 'output']
**output_type_id** | **UUID** | Output type identifier | 
**task_type_id** | **UUID** | Task type identifier | 
**person_id** | **UUID** | Person identifier | [optional] 
**working_file_id** | **UUID** | Source working file identifier | [optional] 
**file_status_id** | **UUID** | File status identifier | [optional] 
**comment** | **str** | Output file comment | [optional] 
**extension** | **str** | File extension | [optional] 
**representation** | **str** | File representation | [optional] 
**revision** | **int** | File revision number | [optional] 
**nb_elements** | **int** | Number of elements | [optional] [default to 1]
**sep** | **str** | Path separator | [optional] [default to '/']

## Example

```python
from sometech.pykitsu._client.models.create_new_entity_output_file_request import CreateNewEntityOutputFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewEntityOutputFileRequest from a JSON string
create_new_entity_output_file_request_instance = CreateNewEntityOutputFileRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNewEntityOutputFileRequest.to_json())

# convert the object into a dict
create_new_entity_output_file_request_dict = create_new_entity_output_file_request_instance.to_dict()
# create an instance of CreateNewEntityOutputFileRequest from a dict
create_new_entity_output_file_request_from_dict = CreateNewEntityOutputFileRequest.from_dict(create_new_entity_output_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


