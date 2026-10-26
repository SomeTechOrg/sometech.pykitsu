# UpdateSubscription200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**entity_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_subscription200_response import UpdateSubscription200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscription200Response from a JSON string
update_subscription200_response_instance = UpdateSubscription200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscription200Response.to_json())

# convert the object into a dict
update_subscription200_response_dict = update_subscription200_response_instance.to_dict()
# create an instance of UpdateSubscription200Response from a dict
update_subscription200_response_from_dict = UpdateSubscription200Response.from_dict(update_subscription200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


