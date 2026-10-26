# GetNextInstanceOutputFileRevisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | File name | [optional] [default to 'main']
**output_type_id** | **UUID** | Output type identifier | 
**task_type_id** | **UUID** | Task type identifier | 

## Example

```python
from sometech.pykitsu._client.models.get_next_instance_output_file_revision_request import GetNextInstanceOutputFileRevisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetNextInstanceOutputFileRevisionRequest from a JSON string
get_next_instance_output_file_revision_request_instance = GetNextInstanceOutputFileRevisionRequest.from_json(json)
# print the JSON string representation of the object
print(GetNextInstanceOutputFileRevisionRequest.to_json())

# convert the object into a dict
get_next_instance_output_file_revision_request_dict = get_next_instance_output_file_revision_request_instance.to_dict()
# create an instance of GetNextInstanceOutputFileRevisionRequest from a dict
get_next_instance_output_file_revision_request_from_dict = GetNextInstanceOutputFileRevisionRequest.from_dict(get_next_instance_output_file_revision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


