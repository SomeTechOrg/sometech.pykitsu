# CreateSearchFilter201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**search_filter_group_id** | **UUID** |  | [optional] 
**list_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_search_filter201_response import CreateSearchFilter201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSearchFilter201Response from a JSON string
create_search_filter201_response_instance = CreateSearchFilter201Response.from_json(json)
# print the JSON string representation of the object
print(CreateSearchFilter201Response.to_json())

# convert the object into a dict
create_search_filter201_response_dict = create_search_filter201_response_instance.to_dict()
# create an instance of CreateSearchFilter201Response from a dict
create_search_filter201_response_from_dict = CreateSearchFilter201Response.from_dict(create_search_filter201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


