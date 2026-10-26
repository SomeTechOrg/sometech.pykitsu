# AddTimeSpentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **float** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.add_time_spent_request import AddTimeSpentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddTimeSpentRequest from a JSON string
add_time_spent_request_instance = AddTimeSpentRequest.from_json(json)
# print the JSON string representation of the object
print(AddTimeSpentRequest.to_json())

# convert the object into a dict
add_time_spent_request_dict = add_time_spent_request_instance.to_dict()
# create an instance of AddTimeSpentRequest from a dict
add_time_spent_request_from_dict = AddTimeSpentRequest.from_dict(add_time_spent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


