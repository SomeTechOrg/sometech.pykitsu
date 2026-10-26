# GetFileInformation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | File unique identifier | [optional] 
**name** | **str** | File name | [optional] 
**path** | **str** | File path | [optional] 
**revision** | **int** | File revision | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**task_id** | **UUID** | Task identifier (for working files) | [optional] 
**entity_id** | **UUID** | Entity identifier (for output files) | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_file_information200_response import GetFileInformation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetFileInformation200Response from a JSON string
get_file_information200_response_instance = GetFileInformation200Response.from_json(json)
# print the JSON string representation of the object
print(GetFileInformation200Response.to_json())

# convert the object into a dict
get_file_information200_response_dict = get_file_information200_response_instance.to_dict()
# create an instance of GetFileInformation200Response from a dict
get_file_information200_response_from_dict = GetFileInformation200Response.from_dict(get_file_information200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


