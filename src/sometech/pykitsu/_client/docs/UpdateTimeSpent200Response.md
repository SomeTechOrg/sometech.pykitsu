# UpdateTimeSpent200Response


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
from sometech.pykitsu._client.models.update_time_spent200_response import UpdateTimeSpent200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTimeSpent200Response from a JSON string
update_time_spent200_response_instance = UpdateTimeSpent200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateTimeSpent200Response.to_json())

# convert the object into a dict
update_time_spent200_response_dict = update_time_spent200_response_instance.to_dict()
# create an instance of UpdateTimeSpent200Response from a dict
update_time_spent200_response_from_dict = UpdateTimeSpent200Response.from_dict(update_time_spent200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


