# ImportTaskTypeEstimationsCsv201ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**estimation** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 
**due_date** | **date** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_task_type_estimations_csv201_response_inner import ImportTaskTypeEstimationsCsv201ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportTaskTypeEstimationsCsv201ResponseInner from a JSON string
import_task_type_estimations_csv201_response_inner_instance = ImportTaskTypeEstimationsCsv201ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ImportTaskTypeEstimationsCsv201ResponseInner.to_json())

# convert the object into a dict
import_task_type_estimations_csv201_response_inner_dict = import_task_type_estimations_csv201_response_inner_instance.to_dict()
# create an instance of ImportTaskTypeEstimationsCsv201ResponseInner from a dict
import_task_type_estimations_csv201_response_inner_from_dict = ImportTaskTypeEstimationsCsv201ResponseInner.from_dict(import_task_type_estimations_csv201_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


