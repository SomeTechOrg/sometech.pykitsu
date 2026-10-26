# CreateFilterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Filter name | 
**query** | **str** | Filter query as JSON string | 
**list_type** | **str** | Type of list this filter applies to | 
**entity_type** | **str** | Entity type this filter applies to | [optional] 
**project_id** | **UUID** | Project identifier | 
**is_shared** | **bool** | Whether to share this filter with others | [optional] [default to False]
**search_filter_group_id** | **UUID** | Filter group identifier | [optional] 
**department_id** | **UUID** | Department identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_filter_request import CreateFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFilterRequest from a JSON string
create_filter_request_instance = CreateFilterRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFilterRequest.to_json())

# convert the object into a dict
create_filter_request_dict = create_filter_request_instance.to_dict()
# create an instance of CreateFilterRequest from a dict
create_filter_request_from_dict = CreateFilterRequest.from_dict(create_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


