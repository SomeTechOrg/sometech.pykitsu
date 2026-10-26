# UpdatePlaylist200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**shots** | **List[object]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_playlist200_response import UpdatePlaylist200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlaylist200Response from a JSON string
update_playlist200_response_instance = UpdatePlaylist200Response.from_json(json)
# print the JSON string representation of the object
print(UpdatePlaylist200Response.to_json())

# convert the object into a dict
update_playlist200_response_dict = update_playlist200_response_instance.to_dict()
# create an instance of UpdatePlaylist200Response from a dict
update_playlist200_response_from_dict = UpdatePlaylist200Response.from_dict(update_playlist200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


