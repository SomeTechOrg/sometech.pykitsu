# GetLastWorkingFiles200ResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Working file unique identifier | [optional] 
**name** | **str** | Working file name | [optional] 
**revision** | **int** | Working file revision | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_last_working_files200_response_value import GetLastWorkingFiles200ResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetLastWorkingFiles200ResponseValue from a JSON string
get_last_working_files200_response_value_instance = GetLastWorkingFiles200ResponseValue.from_json(json)
# print the JSON string representation of the object
print(GetLastWorkingFiles200ResponseValue.to_json())

# convert the object into a dict
get_last_working_files200_response_value_dict = get_last_working_files200_response_value_instance.to_dict()
# create an instance of GetLastWorkingFiles200ResponseValue from a dict
get_last_working_files200_response_value_from_dict = GetLastWorkingFiles200ResponseValue.from_dict(get_last_working_files200_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


