# UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the metadata descriptor | [optional] 
**for_client** | **str** | Whether the descriptor is for client | [optional] [default to 'False']
**choices** | **List[str]** | List of choices for the descriptor | [optional] 
**departments** | **List[str]** | List of departments for the descriptor | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id_request import UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest from a JSON string
update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id_request_instance = UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest.to_json())

# convert the object into a dict
update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id_request_dict = update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id_request_instance.to_dict()
# create an instance of UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest from a dict
update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id_request_from_dict = UpdateMetadataDescriptorPutDataProjectsProjectIdMetadataDescriptorsDescriptorIdRequest.from_dict(update_metadata_descriptor_put_data_projects_project_id_metadata_descriptors_descriptor_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


