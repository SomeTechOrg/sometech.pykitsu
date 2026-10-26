# CreateSearchFilterGroup201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_search_filter_group201_response import CreateSearchFilterGroup201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSearchFilterGroup201Response from a JSON string
create_search_filter_group201_response_instance = CreateSearchFilterGroup201Response.from_json(json)
# print the JSON string representation of the object
print(CreateSearchFilterGroup201Response.to_json())

# convert the object into a dict
create_search_filter_group201_response_dict = create_search_filter_group201_response_instance.to_dict()
# create an instance of CreateSearchFilterGroup201Response from a dict
create_search_filter_group201_response_from_dict = CreateSearchFilterGroup201Response.from_dict(create_search_filter_group201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


