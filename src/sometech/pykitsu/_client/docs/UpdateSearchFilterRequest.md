# UpdateSearchFilterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**list_type** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_search_filter_request import UpdateSearchFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSearchFilterRequest from a JSON string
update_search_filter_request_instance = UpdateSearchFilterRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSearchFilterRequest.to_json())

# convert the object into a dict
update_search_filter_request_dict = update_search_filter_request_instance.to_dict()
# create an instance of UpdateSearchFilterRequest from a dict
update_search_filter_request_from_dict = UpdateSearchFilterRequest.from_dict(update_search_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


