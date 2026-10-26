# CreateProjectSequence201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**episode_id** | **UUID** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_project_sequence201_response import CreateProjectSequence201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectSequence201Response from a JSON string
create_project_sequence201_response_instance = CreateProjectSequence201Response.from_json(json)
# print the JSON string representation of the object
print(CreateProjectSequence201Response.to_json())

# convert the object into a dict
create_project_sequence201_response_dict = create_project_sequence201_response_instance.to_dict()
# create an instance of CreateProjectSequence201Response from a dict
create_project_sequence201_response_from_dict = CreateProjectSequence201Response.from_dict(create_project_sequence201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


