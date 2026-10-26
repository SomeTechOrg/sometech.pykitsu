# GenerateWorkingFilePathRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | File name | [optional] [default to 'main']
**mode** | **str** | File mode | [optional] [default to 'working']
**software_id** | **UUID** | Software identifier | [optional] 
**comment** | **str** | File comment | [optional] 
**revision** | **int** | File revision number | [optional] 
**separator** | **str** | Path separator | [optional] [default to '/']

## Example

```python
from sometech.pykitsu._client.models.generate_working_file_path_request import GenerateWorkingFilePathRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateWorkingFilePathRequest from a JSON string
generate_working_file_path_request_instance = GenerateWorkingFilePathRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateWorkingFilePathRequest.to_json())

# convert the object into a dict
generate_working_file_path_request_dict = generate_working_file_path_request_instance.to_dict()
# create an instance of GenerateWorkingFilePathRequest from a dict
generate_working_file_path_request_from_dict = GenerateWorkingFilePathRequest.from_dict(generate_working_file_path_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


