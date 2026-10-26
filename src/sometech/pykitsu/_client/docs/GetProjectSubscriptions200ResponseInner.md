# GetProjectSubscriptions200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**task_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_project_subscriptions200_response_inner import GetProjectSubscriptions200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectSubscriptions200ResponseInner from a JSON string
get_project_subscriptions200_response_inner_instance = GetProjectSubscriptions200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProjectSubscriptions200ResponseInner.to_json())

# convert the object into a dict
get_project_subscriptions200_response_inner_dict = get_project_subscriptions200_response_inner_instance.to_dict()
# create an instance of GetProjectSubscriptions200ResponseInner from a dict
get_project_subscriptions200_response_inner_from_dict = GetProjectSubscriptions200ResponseInner.from_dict(get_project_subscriptions200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


