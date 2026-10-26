# CreateSearchFilterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**person_id** | **UUID** |  | 
**search_filter_group_id** | **UUID** |  | 
**list_type** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_search_filter_request import CreateSearchFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSearchFilterRequest from a JSON string
create_search_filter_request_instance = CreateSearchFilterRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSearchFilterRequest.to_json())

# convert the object into a dict
create_search_filter_request_dict = create_search_filter_request_instance.to_dict()
# create an instance of CreateSearchFilterRequest from a dict
create_search_filter_request_from_dict = CreateSearchFilterRequest.from_dict(create_search_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


