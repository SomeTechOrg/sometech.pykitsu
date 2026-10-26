# UpdateWorkingFileModificationDate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Working file unique identifier | [optional] 
**updated_at** | **datetime** | Updated modification timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_working_file_modification_date200_response import UpdateWorkingFileModificationDate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkingFileModificationDate200Response from a JSON string
update_working_file_modification_date200_response_instance = UpdateWorkingFileModificationDate200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkingFileModificationDate200Response.to_json())

# convert the object into a dict
update_working_file_modification_date200_response_dict = update_working_file_modification_date200_response_instance.to_dict()
# create an instance of UpdateWorkingFileModificationDate200Response from a dict
update_working_file_modification_date200_response_from_dict = UpdateWorkingFileModificationDate200Response.from_dict(update_working_file_modification_date200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


