# GetInstanceOutputFiles200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Output file unique identifier | [optional] 
**name** | **str** | Output file name | [optional] 
**revision** | **int** | Output file revision | [optional] 
**path** | **str** | Output file path | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**asset_instance_id** | **UUID** | Asset instance identifier | [optional] 
**temporal_entity_id** | **UUID** | Temporal entity identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_instance_output_files200_response_inner import GetInstanceOutputFiles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInstanceOutputFiles200ResponseInner from a JSON string
get_instance_output_files200_response_inner_instance = GetInstanceOutputFiles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetInstanceOutputFiles200ResponseInner.to_json())

# convert the object into a dict
get_instance_output_files200_response_inner_dict = get_instance_output_files200_response_inner_instance.to_dict()
# create an instance of GetInstanceOutputFiles200ResponseInner from a dict
get_instance_output_files200_response_inner_from_dict = GetInstanceOutputFiles200ResponseInner.from_dict(get_instance_output_files200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


