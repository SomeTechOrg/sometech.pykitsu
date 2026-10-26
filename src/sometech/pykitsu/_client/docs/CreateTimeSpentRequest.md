# CreateTimeSpentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **UUID** |  | 
**person_id** | **UUID** |  | 
**var_date** | **date** |  | 
**duration** | **float** |  | 

## Example

```python
from sometech.pykitsu._client.models.create_time_spent_request import CreateTimeSpentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTimeSpentRequest from a JSON string
create_time_spent_request_instance = CreateTimeSpentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTimeSpentRequest.to_json())

# convert the object into a dict
create_time_spent_request_dict = create_time_spent_request_instance.to_dict()
# create an instance of CreateTimeSpentRequest from a dict
create_time_spent_request_from_dict = CreateTimeSpentRequest.from_dict(create_time_spent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


