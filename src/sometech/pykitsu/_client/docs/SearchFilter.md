# SearchFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_type** | **str** | Type of list | [optional] 
**entity_type** | **str** | Type of entity | [optional] 
**name** | **str** | Name of search filter | [optional] 
**search_query** | **str** |  | [optional] 
**person_id** | **UUID** | Person ID | [optional] 
**project_id** | **UUID** | Project ID | [optional] 

## Example

```python
from sometech.pykitsu._client.models.search_filter import SearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFilter from a JSON string
search_filter_instance = SearchFilter.from_json(json)
# print the JSON string representation of the object
print(SearchFilter.to_json())

# convert the object into a dict
search_filter_dict = search_filter_instance.to_dict()
# create an instance of SearchFilter from a dict
search_filter_from_dict = SearchFilter.from_dict(search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


