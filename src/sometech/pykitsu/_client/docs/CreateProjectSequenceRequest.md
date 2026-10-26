# CreateProjectSequenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**episode_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_project_sequence_request import CreateProjectSequenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectSequenceRequest from a JSON string
create_project_sequence_request_instance = CreateProjectSequenceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectSequenceRequest.to_json())

# convert the object into a dict
create_project_sequence_request_dict = create_project_sequence_request_instance.to_dict()
# create an instance of CreateProjectSequenceRequest from a dict
create_project_sequence_request_from_dict = CreateProjectSequenceRequest.from_dict(create_project_sequence_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


