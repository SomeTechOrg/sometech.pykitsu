# UpdateWorkingFileComment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Working file unique identifier | [optional] 
**comment** | **str** | Updated comment | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_working_file_comment200_response import UpdateWorkingFileComment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorkingFileComment200Response from a JSON string
update_working_file_comment200_response_instance = UpdateWorkingFileComment200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateWorkingFileComment200Response.to_json())

# convert the object into a dict
update_working_file_comment200_response_dict = update_working_file_comment200_response_instance.to_dict()
# create an instance of UpdateWorkingFileComment200Response from a dict
update_working_file_comment200_response_from_dict = UpdateWorkingFileComment200Response.from_dict(update_working_file_comment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


