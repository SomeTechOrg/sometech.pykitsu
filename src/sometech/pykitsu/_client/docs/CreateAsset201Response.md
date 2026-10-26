# CreateAsset201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Created asset unique identifier | [optional] 
**name** | **str** | Asset name | [optional] 
**description** | **str** | Asset description | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 
**entity_type_id** | **UUID** | Asset type identifier | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_asset201_response import CreateAsset201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAsset201Response from a JSON string
create_asset201_response_instance = CreateAsset201Response.from_json(json)
# print the JSON string representation of the object
print(CreateAsset201Response.to_json())

# convert the object into a dict
create_asset201_response_dict = create_asset201_response_instance.to_dict()
# create an instance of CreateAsset201Response from a dict
create_asset201_response_from_dict = CreateAsset201Response.from_dict(create_asset201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


