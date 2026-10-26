# CreateFilterGroup201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Filter group unique identifier | [optional] 
**name** | **str** | Filter group name | [optional] 
**color** | **str** | Filter group color | [optional] 
**list_type** | **str** | List type | [optional] 
**entity_type** | **str** | Entity type | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**is_shared** | **bool** | Whether filter group is shared | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_filter_group201_response import CreateFilterGroup201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFilterGroup201Response from a JSON string
create_filter_group201_response_instance = CreateFilterGroup201Response.from_json(json)
# print the JSON string representation of the object
print(CreateFilterGroup201Response.to_json())

# convert the object into a dict
create_filter_group201_response_dict = create_filter_group201_response_instance.to_dict()
# create an instance of CreateFilterGroup201Response from a dict
create_filter_group201_response_from_dict = CreateFilterGroup201Response.from_dict(create_filter_group201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


