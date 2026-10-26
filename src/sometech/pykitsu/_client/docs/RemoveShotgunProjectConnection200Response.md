# RemoveShotgunProjectConnection200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the removal was successful | [optional] 
**removed_instance_id** | **UUID** | ID of the removed connection, if found | [optional] 

## Example

```python
from sometech.pykitsu._client.models.remove_shotgun_project_connection200_response import RemoveShotgunProjectConnection200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveShotgunProjectConnection200Response from a JSON string
remove_shotgun_project_connection200_response_instance = RemoveShotgunProjectConnection200Response.from_json(json)
# print the JSON string representation of the object
print(RemoveShotgunProjectConnection200Response.to_json())

# convert the object into a dict
remove_shotgun_project_connection200_response_dict = remove_shotgun_project_connection200_response_instance.to_dict()
# create an instance of RemoveShotgunProjectConnection200Response from a dict
remove_shotgun_project_connection200_response_from_dict = RemoveShotgunProjectConnection200Response.from_dict(remove_shotgun_project_connection200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


