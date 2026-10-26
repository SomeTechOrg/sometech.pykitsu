# CreateSubscription201Response


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
from sometech.pykitsu._client.models.create_subscription201_response import CreateSubscription201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscription201Response from a JSON string
create_subscription201_response_instance = CreateSubscription201Response.from_json(json)
# print the JSON string representation of the object
print(CreateSubscription201Response.to_json())

# convert the object into a dict
create_subscription201_response_dict = create_subscription201_response_instance.to_dict()
# create an instance of CreateSubscription201Response from a dict
create_subscription201_response_from_dict = CreateSubscription201Response.from_dict(create_subscription201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


