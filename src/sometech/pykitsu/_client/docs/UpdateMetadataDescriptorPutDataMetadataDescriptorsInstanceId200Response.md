# UpdateMetadataDescriptorPutDataMetadataDescriptorsInstanceId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**name** | **str** |  | [optional] 
**field_name** | **str** |  | [optional] 
**data_type** | **str** |  | [optional] 
**project_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_metadata_descriptor_put_data_metadata_descriptors_instance_id200_response import UpdateMetadataDescriptorPutDataMetadataDescriptorsInstanceId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMetadataDescriptorPutDataMetadataDescriptorsInstanceId200Response from a JSON string
update_metadata_descriptor_put_data_metadata_descriptors_instance_id200_response_instance = UpdateMetadataDescriptorPutDataMetadataDescriptorsInstanceId200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateMetadataDescriptorPutDataMetadataDescriptorsInstanceId200Response.to_json())

# convert the object into a dict
update_metadata_descriptor_put_data_metadata_descriptors_instance_id200_response_dict = update_metadata_descriptor_put_data_metadata_descriptors_instance_id200_response_instance.to_dict()
# create an instance of UpdateMetadataDescriptorPutDataMetadataDescriptorsInstanceId200Response from a dict
update_metadata_descriptor_put_data_metadata_descriptors_instance_id200_response_from_dict = UpdateMetadataDescriptorPutDataMetadataDescriptorsInstanceId200Response.from_dict(update_metadata_descriptor_put_data_metadata_descriptors_instance_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


