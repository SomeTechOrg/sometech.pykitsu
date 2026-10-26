# UpdateProject200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**production_type** | **str** |  | [optional] 
**production_style** | **str** |  | [optional] 
**project_status_id** | **UUID** |  | [optional] 
**first_episode_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_project200_response import UpdateProject200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProject200Response from a JSON string
update_project200_response_instance = UpdateProject200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateProject200Response.to_json())

# convert the object into a dict
update_project200_response_dict = update_project200_response_instance.to_dict()
# create an instance of UpdateProject200Response from a dict
update_project200_response_from_dict = UpdateProject200Response.from_dict(update_project200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


