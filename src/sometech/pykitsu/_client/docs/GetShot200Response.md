# GetShot200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**parent_id** | **UUID** |  | [optional] 
**nb_frames** | **int** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_shot200_response import GetShot200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetShot200Response from a JSON string
get_shot200_response_instance = GetShot200Response.from_json(json)
# print the JSON string representation of the object
print(GetShot200Response.to_json())

# convert the object into a dict
get_shot200_response_dict = get_shot200_response_instance.to_dict()
# create an instance of GetShot200Response from a dict
get_shot200_response_from_dict = GetShot200Response.from_dict(get_shot200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


