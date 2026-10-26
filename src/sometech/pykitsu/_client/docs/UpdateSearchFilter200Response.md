# UpdateSearchFilter200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**search_filter_group_id** | **UUID** |  | [optional] 
**list_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_search_filter200_response import UpdateSearchFilter200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSearchFilter200Response from a JSON string
update_search_filter200_response_instance = UpdateSearchFilter200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateSearchFilter200Response.to_json())

# convert the object into a dict
update_search_filter200_response_dict = update_search_filter200_response_instance.to_dict()
# create an instance of UpdateSearchFilter200Response from a dict
update_search_filter200_response_from_dict = UpdateSearchFilter200Response.from_dict(update_search_filter200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


