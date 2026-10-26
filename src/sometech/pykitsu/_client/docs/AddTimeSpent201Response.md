# AddTimeSpent201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**task_id** | **UUID** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**var_date** | **date** |  | [optional] 
**duration** | **float** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.add_time_spent201_response import AddTimeSpent201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddTimeSpent201Response from a JSON string
add_time_spent201_response_instance = AddTimeSpent201Response.from_json(json)
# print the JSON string representation of the object
print(AddTimeSpent201Response.to_json())

# convert the object into a dict
add_time_spent201_response_dict = add_time_spent201_response_instance.to_dict()
# create an instance of AddTimeSpent201Response from a dict
add_time_spent201_response_from_dict = AddTimeSpent201Response.from_dict(add_time_spent201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


