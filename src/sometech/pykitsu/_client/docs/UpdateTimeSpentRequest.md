# UpdateTimeSpentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**duration** | **float** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_time_spent_request import UpdateTimeSpentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTimeSpentRequest from a JSON string
update_time_spent_request_instance = UpdateTimeSpentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTimeSpentRequest.to_json())

# convert the object into a dict
update_time_spent_request_dict = update_time_spent_request_instance.to_dict()
# create an instance of UpdateTimeSpentRequest from a dict
update_time_spent_request_from_dict = UpdateTimeSpentRequest.from_dict(update_time_spent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


