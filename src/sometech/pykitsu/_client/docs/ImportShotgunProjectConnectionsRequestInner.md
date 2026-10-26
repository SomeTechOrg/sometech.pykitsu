# ImportShotgunProjectConnectionsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the connection | [optional] 
**project** | [**ImportShotgunAssetsRequestInnerProject**](ImportShotgunAssetsRequestInnerProject.md) |  | [optional] 
**user** | [**ImportShotgunVersionsRequestInnerUser**](ImportShotgunVersionsRequestInnerUser.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_project_connections_request_inner import ImportShotgunProjectConnectionsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunProjectConnectionsRequestInner from a JSON string
import_shotgun_project_connections_request_inner_instance = ImportShotgunProjectConnectionsRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunProjectConnectionsRequestInner.to_json())

# convert the object into a dict
import_shotgun_project_connections_request_inner_dict = import_shotgun_project_connections_request_inner_instance.to_dict()
# create an instance of ImportShotgunProjectConnectionsRequestInner from a dict
import_shotgun_project_connections_request_inner_from_dict = ImportShotgunProjectConnectionsRequestInner.from_dict(import_shotgun_project_connections_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


