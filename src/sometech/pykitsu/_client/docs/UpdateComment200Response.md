# UpdateComment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**object_id** | **UUID** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**task_status_id** | **UUID** |  | [optional] 
**text** | **str** |  | [optional] 
**pinned** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_comment200_response import UpdateComment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateComment200Response from a JSON string
update_comment200_response_instance = UpdateComment200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateComment200Response.to_json())

# convert the object into a dict
update_comment200_response_dict = update_comment200_response_instance.to_dict()
# create an instance of UpdateComment200Response from a dict
update_comment200_response_from_dict = UpdateComment200Response.from_dict(update_comment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


