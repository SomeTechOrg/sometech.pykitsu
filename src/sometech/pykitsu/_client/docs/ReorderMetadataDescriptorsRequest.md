# ReorderMetadataDescriptorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Entity type for the metadata descriptors | 
**descriptor_ids** | **List[UUID]** | List of metadata descriptor IDs in the desired order | 

## Example

```python
from sometech.pykitsu._client.models.reorder_metadata_descriptors_request import ReorderMetadataDescriptorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderMetadataDescriptorsRequest from a JSON string
reorder_metadata_descriptors_request_instance = ReorderMetadataDescriptorsRequest.from_json(json)
# print the JSON string representation of the object
print(ReorderMetadataDescriptorsRequest.to_json())

# convert the object into a dict
reorder_metadata_descriptors_request_dict = reorder_metadata_descriptors_request_instance.to_dict()
# create an instance of ReorderMetadataDescriptorsRequest from a dict
reorder_metadata_descriptors_request_from_dict = ReorderMetadataDescriptorsRequest.from_dict(reorder_metadata_descriptors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


