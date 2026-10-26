# GetEntityTimeSpent200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Time spent unique identifier | [optional] 
**duration** | **float** | Time duration in hours | [optional] 
**var_date** | **date** | Date when time was spent | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**person_id** | **UUID** | Person identifier who spent the time | [optional] 
**entity_id** | **UUID** | Entity identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_entity_time_spent200_response_inner import GetEntityTimeSpent200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityTimeSpent200ResponseInner from a JSON string
get_entity_time_spent200_response_inner_instance = GetEntityTimeSpent200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetEntityTimeSpent200ResponseInner.to_json())

# convert the object into a dict
get_entity_time_spent200_response_inner_dict = get_entity_time_spent200_response_inner_instance.to_dict()
# create an instance of GetEntityTimeSpent200ResponseInner from a dict
get_entity_time_spent200_response_inner_from_dict = GetEntityTimeSpent200ResponseInner.from_dict(get_entity_time_spent200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


