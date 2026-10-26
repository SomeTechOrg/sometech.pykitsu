# CreateMetadataDescriptorPostDataMetadataDescriptorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**field_name** | **str** |  | 
**data_type** | **str** |  | 
**project_id** | **UUID** |  | 
**entity_type** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_metadata_descriptor_post_data_metadata_descriptors_request import CreateMetadataDescriptorPostDataMetadataDescriptorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMetadataDescriptorPostDataMetadataDescriptorsRequest from a JSON string
create_metadata_descriptor_post_data_metadata_descriptors_request_instance = CreateMetadataDescriptorPostDataMetadataDescriptorsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMetadataDescriptorPostDataMetadataDescriptorsRequest.to_json())

# convert the object into a dict
create_metadata_descriptor_post_data_metadata_descriptors_request_dict = create_metadata_descriptor_post_data_metadata_descriptors_request_instance.to_dict()
# create an instance of CreateMetadataDescriptorPostDataMetadataDescriptorsRequest from a dict
create_metadata_descriptor_post_data_metadata_descriptors_request_from_dict = CreateMetadataDescriptorPostDataMetadataDescriptorsRequest.from_dict(create_metadata_descriptor_post_data_metadata_descriptors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


