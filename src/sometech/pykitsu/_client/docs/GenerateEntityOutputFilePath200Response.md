# GenerateEntityOutputFilePath200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_path** | **str** | Generated folder path | [optional] 
**file_name** | **str** | Generated file name | [optional] 

## Example

```python
from sometech.pykitsu._client.models.generate_entity_output_file_path200_response import GenerateEntityOutputFilePath200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateEntityOutputFilePath200Response from a JSON string
generate_entity_output_file_path200_response_instance = GenerateEntityOutputFilePath200Response.from_json(json)
# print the JSON string representation of the object
print(GenerateEntityOutputFilePath200Response.to_json())

# convert the object into a dict
generate_entity_output_file_path200_response_dict = generate_entity_output_file_path200_response_instance.to_dict()
# create an instance of GenerateEntityOutputFilePath200Response from a dict
generate_entity_output_file_path200_response_from_dict = GenerateEntityOutputFilePath200Response.from_dict(generate_entity_output_file_path200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


