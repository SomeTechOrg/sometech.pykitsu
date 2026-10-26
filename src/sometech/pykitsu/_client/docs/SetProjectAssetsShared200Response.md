# SetProjectAssetsShared200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_count** | **int** | Number of assets updated | [optional] 
**project_id** | **UUID** | Project identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.set_project_assets_shared200_response import SetProjectAssetsShared200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetProjectAssetsShared200Response from a JSON string
set_project_assets_shared200_response_instance = SetProjectAssetsShared200Response.from_json(json)
# print the JSON string representation of the object
print(SetProjectAssetsShared200Response.to_json())

# convert the object into a dict
set_project_assets_shared200_response_dict = set_project_assets_shared200_response_instance.to_dict()
# create an instance of SetProjectAssetsShared200Response from a dict
set_project_assets_shared200_response_from_dict = SetProjectAssetsShared200Response.from_dict(set_project_assets_shared200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


