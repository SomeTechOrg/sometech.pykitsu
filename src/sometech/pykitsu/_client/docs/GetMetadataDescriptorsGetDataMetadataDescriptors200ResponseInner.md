# GetMetadataDescriptorsGetDataMetadataDescriptors200ResponseInner


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
from sometech.pykitsu._client.models.get_metadata_descriptors_get_data_metadata_descriptors200_response_inner import GetMetadataDescriptorsGetDataMetadataDescriptors200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetadataDescriptorsGetDataMetadataDescriptors200ResponseInner from a JSON string
get_metadata_descriptors_get_data_metadata_descriptors200_response_inner_instance = GetMetadataDescriptorsGetDataMetadataDescriptors200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetMetadataDescriptorsGetDataMetadataDescriptors200ResponseInner.to_json())

# convert the object into a dict
get_metadata_descriptors_get_data_metadata_descriptors200_response_inner_dict = get_metadata_descriptors_get_data_metadata_descriptors200_response_inner_instance.to_dict()
# create an instance of GetMetadataDescriptorsGetDataMetadataDescriptors200ResponseInner from a dict
get_metadata_descriptors_get_data_metadata_descriptors200_response_inner_from_dict = GetMetadataDescriptorsGetDataMetadataDescriptors200ResponseInner.from_dict(get_metadata_descriptors_get_data_metadata_descriptors200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


