# CreateFilterGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Filter group name | 
**color** | **str** | Filter group color in hex format | 
**list_type** | **str** | Type of list this filter group applies to | 
**entity_type** | **str** | Entity type this filter group applies to | [optional] 
**is_shared** | **bool** | Whether to share this filter group with others | [optional] [default to False]
**project_id** | **UUID** | Project identifier | 
**department_id** | **UUID** | Department identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_filter_group_request import CreateFilterGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFilterGroupRequest from a JSON string
create_filter_group_request_instance = CreateFilterGroupRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFilterGroupRequest.to_json())

# convert the object into a dict
create_filter_group_request_dict = create_filter_group_request_instance.to_dict()
# create an instance of CreateFilterGroupRequest from a dict
create_filter_group_request_from_dict = CreateFilterGroupRequest.from_dict(create_filter_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


