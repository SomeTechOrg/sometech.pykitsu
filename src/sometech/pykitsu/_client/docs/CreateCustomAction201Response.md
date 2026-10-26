# CreateCustomAction201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**url_pattern** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_custom_action201_response import CreateCustomAction201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomAction201Response from a JSON string
create_custom_action201_response_instance = CreateCustomAction201Response.from_json(json)
# print the JSON string representation of the object
print(CreateCustomAction201Response.to_json())

# convert the object into a dict
create_custom_action201_response_dict = create_custom_action201_response_instance.to_dict()
# create an instance of CreateCustomAction201Response from a dict
create_custom_action201_response_from_dict = CreateCustomAction201Response.from_dict(create_custom_action201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


