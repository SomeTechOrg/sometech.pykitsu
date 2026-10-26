# CreateEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Edit name | 
**description** | **str** | Edit description | [optional] 
**data** | **object** | Additional edit data | [optional] 
**episode_id** | **UUID** | Episode identifier (optional) | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_edit_request import CreateEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEditRequest from a JSON string
create_edit_request_instance = CreateEditRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEditRequest.to_json())

# convert the object into a dict
create_edit_request_dict = create_edit_request_instance.to_dict()
# create an instance of CreateEditRequest from a dict
create_edit_request_from_dict = CreateEditRequest.from_dict(create_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


