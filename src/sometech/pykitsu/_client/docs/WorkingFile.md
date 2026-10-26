# WorkingFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 
**name** | **str** | Name of working file | [optional] 
**description** | **str** | working file brief | [optional] 
**comment** | **str** | Comment on working file | [optional] 
**revision** | **int** | Revision number of working file | [optional] 
**size** | **int** | Size of working file | [optional] 
**checksum** | **str** | Checksum of working file | [optional] 
**path** | **str** | File path on the production hard drive | [optional] 
**data** | **str** | Free JSON field to add metadata | [optional] 
**task_id** | **UUID** | Task for which the working file is made | [optional] 
**entity_id** | **UUID** | Entity for which the working is made | [optional] 
**person_id** | **UUID** | Author of the file | [optional] 
**software_id** | **UUID** | Software used to build this working file | [optional] 
**id** | **UUID** | Working file unique identifier | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.working_file import WorkingFile

# TODO update the JSON string below
json = "{}"
# create an instance of WorkingFile from a JSON string
working_file_instance = WorkingFile.from_json(json)
# print the JSON string representation of the object
print(WorkingFile.to_json())

# convert the object into a dict
working_file_dict = working_file_instance.to_dict()
# create an instance of WorkingFile from a dict
working_file_from_dict = WorkingFile.from_dict(working_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


