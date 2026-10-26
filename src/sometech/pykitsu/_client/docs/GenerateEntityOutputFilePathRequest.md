# GenerateEntityOutputFilePathRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | File name | [optional] [default to 'main']
**mode** | **str** | File mode | [optional] [default to 'output']
**output_type_id** | **UUID** | Output type identifier | 
**task_type_id** | **UUID** | Task type identifier | 
**extension** | **str** | File extension | [optional] 
**representation** | **str** | File representation | [optional] 
**revision** | **int** | File revision number | [optional] 
**separator** | **str** | Path separator | [optional] [default to '/']

## Example

```python
from sometech.pykitsu._client.models.generate_entity_output_file_path_request import GenerateEntityOutputFilePathRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateEntityOutputFilePathRequest from a JSON string
generate_entity_output_file_path_request_instance = GenerateEntityOutputFilePathRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateEntityOutputFilePathRequest.to_json())

# convert the object into a dict
generate_entity_output_file_path_request_dict = generate_entity_output_file_path_request_instance.to_dict()
# create an instance of GenerateEntityOutputFilePathRequest from a dict
generate_entity_output_file_path_request_from_dict = GenerateEntityOutputFilePathRequest.from_dict(generate_entity_output_file_path_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


