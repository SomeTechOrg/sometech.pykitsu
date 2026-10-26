# PreviewFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 
**name** | **str** | Name of preview file | [optional] 
**original_name** | **str** | Original name of preview file | [optional] 
**revision** | **int** | Revision number of preview file | [optional] 
**position** | **int** | Position of preview file | [optional] 
**extension** | **str** | Extension of preview file | [optional] 
**description** | **str** | Preview file brief | [optional] 
**path** | **str** | File path on the production hard drive | [optional] 
**source** | **str** | Created by a script, a webgui or a desktop gui | [optional] 
**file_size** | **int** | Size of output file | [optional] 
**comment** | **str** | Comment on output file | [optional] 
**checksum** | **str** | Checksum of output file | [optional] 
**representation** | **str** | Precise what kind of output it is (abc, jpgs, pngs, etc.) | [optional] 
**nb_elements** | **int** | For image sequence | [optional] 
**canceled** | **bool** |  | [optional] 
**file_status_id** | **UUID** | File status ID | [optional] 
**entity_id** | **UUID** | Asset or Shot concerned by the output file | [optional] 
**asset_instance_id** | **UUID** | Asset instance ID | [optional] 
**output_type_id** | **UUID** | Type of output (geometry, cache, etc.) | [optional] 
**task_type_id** | **UUID** | Task type related to this output file (modeling, animation, etc.) | [optional] 
**person_id** | **UUID** | Author of the file | [optional] 
**source_file_id** | **UUID** | Working file that led to create this output file | [optional] 
**temporal_entity_id** | **UUID** | Shot, scene or sequence needed for output files related to an asset instance | [optional] 
**data** | **str** | Free JSON field to add metadata | [optional] 

## Example

```python
from sometech.pykitsu._client.models.preview_file import PreviewFile

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewFile from a JSON string
preview_file_instance = PreviewFile.from_json(json)
# print the JSON string representation of the object
print(PreviewFile.to_json())

# convert the object into a dict
preview_file_dict = preview_file_instance.to_dict()
# create an instance of PreviewFile from a dict
preview_file_from_dict = PreviewFile.from_dict(preview_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


