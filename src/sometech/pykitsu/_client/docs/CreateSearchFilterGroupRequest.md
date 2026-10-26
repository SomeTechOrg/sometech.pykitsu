# CreateSearchFilterGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**person_id** | **UUID** |  | 

## Example

```python
from sometech.pykitsu._client.models.create_search_filter_group_request import CreateSearchFilterGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSearchFilterGroupRequest from a JSON string
create_search_filter_group_request_instance = CreateSearchFilterGroupRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSearchFilterGroupRequest.to_json())

# convert the object into a dict
create_search_filter_group_request_dict = create_search_filter_group_request_instance.to_dict()
# create an instance of CreateSearchFilterGroupRequest from a dict
create_search_filter_group_request_from_dict = CreateSearchFilterGroupRequest.from_dict(create_search_filter_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


