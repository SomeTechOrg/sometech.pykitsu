# SubscribeToSequence201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Subscription unique identifier | [optional] 
**person_id** | **UUID** | Person identifier | [optional] 
**sequence_id** | **UUID** | Sequence identifier | [optional] 
**task_type_id** | **UUID** | Task type identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.subscribe_to_sequence201_response import SubscribeToSequence201Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribeToSequence201Response from a JSON string
subscribe_to_sequence201_response_instance = SubscribeToSequence201Response.from_json(json)
# print the JSON string representation of the object
print(SubscribeToSequence201Response.to_json())

# convert the object into a dict
subscribe_to_sequence201_response_dict = subscribe_to_sequence201_response_instance.to_dict()
# create an instance of SubscribeToSequence201Response from a dict
subscribe_to_sequence201_response_from_dict = SubscribeToSequence201Response.from_dict(subscribe_to_sequence201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


