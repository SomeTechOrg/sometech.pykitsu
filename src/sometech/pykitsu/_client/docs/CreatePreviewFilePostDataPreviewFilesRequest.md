# CreatePreviewFilePostDataPreviewFilesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**task_id** | **UUID** |  | 
**revision** | **int** |  | [optional] [default to 1]

## Example

```python
from sometech.pykitsu._client.models.create_preview_file_post_data_preview_files_request import CreatePreviewFilePostDataPreviewFilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePreviewFilePostDataPreviewFilesRequest from a JSON string
create_preview_file_post_data_preview_files_request_instance = CreatePreviewFilePostDataPreviewFilesRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePreviewFilePostDataPreviewFilesRequest.to_json())

# convert the object into a dict
create_preview_file_post_data_preview_files_request_dict = create_preview_file_post_data_preview_files_request_instance.to_dict()
# create an instance of CreatePreviewFilePostDataPreviewFilesRequest from a dict
create_preview_file_post_data_preview_files_request_from_dict = CreatePreviewFilePostDataPreviewFilesRequest.from_dict(create_preview_file_post_data_preview_files_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


