# UpdateFilter200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Filter unique identifier | [optional] 
**name** | **str** | Filter name | [optional] 
**query** | **str** | Filter query JSON | [optional] 
**list_type** | **str** | List type | [optional] 
**entity_type** | **str** | Entity type | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**is_shared** | **bool** | Whether filter is shared | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_filter200_response import UpdateFilter200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFilter200Response from a JSON string
update_filter200_response_instance = UpdateFilter200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateFilter200Response.to_json())

# convert the object into a dict
update_filter200_response_dict = update_filter200_response_instance.to_dict()
# create an instance of UpdateFilter200Response from a dict
update_filter200_response_from_dict = UpdateFilter200Response.from_dict(update_filter200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


