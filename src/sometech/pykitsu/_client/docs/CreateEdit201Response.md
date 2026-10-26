# CreateEdit201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Edit unique identifier | [optional] 
**name** | **str** | Edit name | [optional] 
**description** | **str** | Edit description | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**episode_id** | **UUID** | Episode identifier | [optional] 
**data** | **object** | Additional edit data | [optional] 
**created_by** | **UUID** | Creator person identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_edit201_response import CreateEdit201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEdit201Response from a JSON string
create_edit201_response_instance = CreateEdit201Response.from_json(json)
# print the JSON string representation of the object
print(CreateEdit201Response.to_json())

# convert the object into a dict
create_edit201_response_dict = create_edit201_response_instance.to_dict()
# create an instance of CreateEdit201Response from a dict
create_edit201_response_from_dict = CreateEdit201Response.from_dict(create_edit201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


