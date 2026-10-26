# CreateMetadataDescriptorPostDataMetadataDescriptors201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**field_name** | **str** |  | [optional] 
**data_type** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_metadata_descriptor_post_data_metadata_descriptors201_response import CreateMetadataDescriptorPostDataMetadataDescriptors201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMetadataDescriptorPostDataMetadataDescriptors201Response from a JSON string
create_metadata_descriptor_post_data_metadata_descriptors201_response_instance = CreateMetadataDescriptorPostDataMetadataDescriptors201Response.from_json(json)
# print the JSON string representation of the object
print(CreateMetadataDescriptorPostDataMetadataDescriptors201Response.to_json())

# convert the object into a dict
create_metadata_descriptor_post_data_metadata_descriptors201_response_dict = create_metadata_descriptor_post_data_metadata_descriptors201_response_instance.to_dict()
# create an instance of CreateMetadataDescriptorPostDataMetadataDescriptors201Response from a dict
create_metadata_descriptor_post_data_metadata_descriptors201_response_from_dict = CreateMetadataDescriptorPostDataMetadataDescriptors201Response.from_dict(create_metadata_descriptor_post_data_metadata_descriptors201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


