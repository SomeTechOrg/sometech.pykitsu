# GetLastInstanceOutputFiles200ResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Output file unique identifier | [optional] 
**name** | **str** | Output file name | [optional] 
**revision** | **int** | Output file revision | [optional] 
**path** | **str** | Output file path | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_last_instance_output_files200_response_value import GetLastInstanceOutputFiles200ResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetLastInstanceOutputFiles200ResponseValue from a JSON string
get_last_instance_output_files200_response_value_instance = GetLastInstanceOutputFiles200ResponseValue.from_json(json)
# print the JSON string representation of the object
print(GetLastInstanceOutputFiles200ResponseValue.to_json())

# convert the object into a dict
get_last_instance_output_files200_response_value_dict = get_last_instance_output_files200_response_value_instance.to_dict()
# create an instance of GetLastInstanceOutputFiles200ResponseValue from a dict
get_last_instance_output_files200_response_value_from_dict = GetLastInstanceOutputFiles200ResponseValue.from_dict(get_last_instance_output_files200_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


