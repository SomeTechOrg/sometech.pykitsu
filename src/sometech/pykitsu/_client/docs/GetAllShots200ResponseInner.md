# GetAllShots200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**parent_id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_all_shots200_response_inner import GetAllShots200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllShots200ResponseInner from a JSON string
get_all_shots200_response_inner_instance = GetAllShots200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetAllShots200ResponseInner.to_json())

# convert the object into a dict
get_all_shots200_response_inner_dict = get_all_shots200_response_inner_instance.to_dict()
# create an instance of GetAllShots200ResponseInner from a dict
get_all_shots200_response_inner_from_dict = GetAllShots200ResponseInner.from_dict(get_all_shots200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


