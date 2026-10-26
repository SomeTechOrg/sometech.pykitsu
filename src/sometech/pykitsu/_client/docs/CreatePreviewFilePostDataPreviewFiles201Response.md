# CreatePreviewFilePostDataPreviewFiles201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**task_id** | **UUID** |  | [optional] 
**revision** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_preview_file_post_data_preview_files201_response import CreatePreviewFilePostDataPreviewFiles201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePreviewFilePostDataPreviewFiles201Response from a JSON string
create_preview_file_post_data_preview_files201_response_instance = CreatePreviewFilePostDataPreviewFiles201Response.from_json(json)
# print the JSON string representation of the object
print(CreatePreviewFilePostDataPreviewFiles201Response.to_json())

# convert the object into a dict
create_preview_file_post_data_preview_files201_response_dict = create_preview_file_post_data_preview_files201_response_instance.to_dict()
# create an instance of CreatePreviewFilePostDataPreviewFiles201Response from a dict
create_preview_file_post_data_preview_files201_response_from_dict = CreatePreviewFilePostDataPreviewFiles201Response.from_dict(create_preview_file_post_data_preview_files201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


