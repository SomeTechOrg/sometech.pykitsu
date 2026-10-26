# RemoveShotgunStep200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the removal was successful | [optional] 
**removed_instance_id** | **UUID** | ID of the removed step, if found | [optional] 

## Example

```python
from sometech.pykitsu._client.models.remove_shotgun_step200_response import RemoveShotgunStep200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveShotgunStep200Response from a JSON string
remove_shotgun_step200_response_instance = RemoveShotgunStep200Response.from_json(json)
# print the JSON string representation of the object
print(RemoveShotgunStep200Response.to_json())

# convert the object into a dict
remove_shotgun_step200_response_dict = remove_shotgun_step200_response_instance.to_dict()
# create an instance of RemoveShotgunStep200Response from a dict
remove_shotgun_step200_response_from_dict = RemoveShotgunStep200Response.from_dict(remove_shotgun_step200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


