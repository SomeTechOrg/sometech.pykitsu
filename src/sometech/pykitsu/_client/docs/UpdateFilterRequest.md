# UpdateFilterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Filter name | [optional] 
**search_query** | **str** | Updated filter query | [optional] 
**search_filter_group_id** | **UUID** | Filter group identifier | [optional] 
**is_shared** | **bool** | Whether to share this filter | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**department_id** | **UUID** | Department identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_filter_request import UpdateFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFilterRequest from a JSON string
update_filter_request_instance = UpdateFilterRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFilterRequest.to_json())

# convert the object into a dict
update_filter_request_dict = update_filter_request_instance.to_dict()
# create an instance of UpdateFilterRequest from a dict
update_filter_request_from_dict = UpdateFilterRequest.from_dict(update_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


