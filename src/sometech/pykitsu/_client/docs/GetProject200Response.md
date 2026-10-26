# GetProject200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**production_type** | **str** |  | [optional] 
**production_style** | **str** |  | [optional] 
**project_status_id** | **UUID** |  | [optional] 
**project_status_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project200_response import GetProject200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProject200Response from a JSON string
get_project200_response_instance = GetProject200Response.from_json(json)
# print the JSON string representation of the object
print(GetProject200Response.to_json())

# convert the object into a dict
get_project200_response_dict = get_project200_response_instance.to_dict()
# create an instance of GetProject200Response from a dict
get_project200_response_from_dict = GetProject200Response.from_dict(get_project200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


