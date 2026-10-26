# SetTimeSpentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **float** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_time_spent_request import SetTimeSpentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTimeSpentRequest from a JSON string
set_time_spent_request_instance = SetTimeSpentRequest.from_json(json)
# print the JSON string representation of the object
print(SetTimeSpentRequest.to_json())

# convert the object into a dict
set_time_spent_request_dict = set_time_spent_request_instance.to_dict()
# create an instance of SetTimeSpentRequest from a dict
set_time_spent_request_from_dict = SetTimeSpentRequest.from_dict(set_time_spent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


