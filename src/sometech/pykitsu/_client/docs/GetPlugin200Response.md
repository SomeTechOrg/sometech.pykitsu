# GetPlugin200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_plugin200_response import GetPlugin200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlugin200Response from a JSON string
get_plugin200_response_instance = GetPlugin200Response.from_json(json)
# print the JSON string representation of the object
print(GetPlugin200Response.to_json())

# convert the object into a dict
get_plugin200_response_dict = get_plugin200_response_instance.to_dict()
# create an instance of GetPlugin200Response from a dict
get_plugin200_response_from_dict = GetPlugin200Response.from_dict(get_plugin200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


