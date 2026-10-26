# CreateTimeSpent201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**task_id** | **UUID** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**var_date** | **date** |  | [optional] 
**duration** | **float** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_time_spent201_response import CreateTimeSpent201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTimeSpent201Response from a JSON string
create_time_spent201_response_instance = CreateTimeSpent201Response.from_json(json)
# print the JSON string representation of the object
print(CreateTimeSpent201Response.to_json())

# convert the object into a dict
create_time_spent201_response_dict = create_time_spent201_response_instance.to_dict()
# create an instance of CreateTimeSpent201Response from a dict
create_time_spent201_response_from_dict = CreateTimeSpent201Response.from_dict(create_time_spent201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


