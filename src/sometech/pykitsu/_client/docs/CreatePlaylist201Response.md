# CreatePlaylist201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**episode_id** | **UUID** |  | [optional] 
**task_type_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_playlist201_response import CreatePlaylist201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlaylist201Response from a JSON string
create_playlist201_response_instance = CreatePlaylist201Response.from_json(json)
# print the JSON string representation of the object
print(CreatePlaylist201Response.to_json())

# convert the object into a dict
create_playlist201_response_dict = create_playlist201_response_instance.to_dict()
# create an instance of CreatePlaylist201Response from a dict
create_playlist201_response_from_dict = CreatePlaylist201Response.from_dict(create_playlist201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


