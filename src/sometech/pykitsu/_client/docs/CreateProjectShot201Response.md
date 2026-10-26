# CreateProjectShot201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**sequence_id** | **UUID** |  | [optional] 
**nb_frames** | **int** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_project_shot201_response import CreateProjectShot201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectShot201Response from a JSON string
create_project_shot201_response_instance = CreateProjectShot201Response.from_json(json)
# print the JSON string representation of the object
print(CreateProjectShot201Response.to_json())

# convert the object into a dict
create_project_shot201_response_dict = create_project_shot201_response_instance.to_dict()
# create an instance of CreateProjectShot201Response from a dict
create_project_shot201_response_from_dict = CreateProjectShot201Response.from_dict(create_project_shot201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


