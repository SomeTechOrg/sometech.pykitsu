# SubscribeToTask201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Subscription unique identifier | [optional] 
**person_id** | **UUID** | Person identifier | [optional] 
**task_id** | **UUID** | Task identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.subscribe_to_task201_response import SubscribeToTask201Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribeToTask201Response from a JSON string
subscribe_to_task201_response_instance = SubscribeToTask201Response.from_json(json)
# print the JSON string representation of the object
print(SubscribeToTask201Response.to_json())

# convert the object into a dict
subscribe_to_task201_response_dict = subscribe_to_task201_response_instance.to_dict()
# create an instance of SubscribeToTask201Response from a dict
subscribe_to_task201_response_from_dict = SubscribeToTask201Response.from_dict(subscribe_to_task201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


