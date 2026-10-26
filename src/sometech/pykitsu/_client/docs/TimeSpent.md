# TimeSpent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **float** |  | [optional] 
**var_date** | **date** |  | [optional] 
**task_id** | **UUID** | Related task ID | [optional] 
**person_id** | **UUID** | The person who performed the working time | [optional] 
**id** | **UUID** | Time spent unique identifier | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.time_spent import TimeSpent

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSpent from a JSON string
time_spent_instance = TimeSpent.from_json(json)
# print the JSON string representation of the object
print(TimeSpent.to_json())

# convert the object into a dict
time_spent_dict = time_spent_instance.to_dict()
# create an instance of TimeSpent from a dict
time_spent_from_dict = TimeSpent.from_dict(time_spent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


