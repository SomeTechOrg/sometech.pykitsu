# UpdateFilterGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Filter group name | [optional] 
**color** | **str** | Filter group color | [optional] 
**is_shared** | **bool** | Whether to share this filter group | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**department_id** | **UUID** | Department identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_filter_group_request import UpdateFilterGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFilterGroupRequest from a JSON string
update_filter_group_request_instance = UpdateFilterGroupRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFilterGroupRequest.to_json())

# convert the object into a dict
update_filter_group_request_dict = update_filter_group_request_instance.to_dict()
# create an instance of UpdateFilterGroupRequest from a dict
update_filter_group_request_from_dict = UpdateFilterGroupRequest.from_dict(update_filter_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


