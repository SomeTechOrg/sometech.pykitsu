# CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Entity type for the metadata descriptor | [optional] [default to 'Asset']
**name** | **str** | Name of the metadata descriptor | 
**data_type** | **str** | Type of data (string, number, boolean, etc.) | 
**for_client** | **str** | Whether the descriptor is for client | [optional] [default to 'False']
**choices** | **List[str]** | List of choices for the descriptor | [optional] 
**departments** | **List[str]** | List of departments for the descriptor | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors_request import CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest from a JSON string
create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors_request_instance = CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest.to_json())

# convert the object into a dict
create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors_request_dict = create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors_request_instance.to_dict()
# create an instance of CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest from a dict
create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors_request_from_dict = CreateMetadataDescriptorPostDataProjectsProjectIdMetadataDescriptorsRequest.from_dict(create_metadata_descriptor_post_data_projects_project_id_metadata_descriptors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


