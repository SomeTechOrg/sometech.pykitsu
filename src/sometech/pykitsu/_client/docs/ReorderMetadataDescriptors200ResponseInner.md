# ReorderMetadataDescriptors200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Metadata descriptor unique identifier | [optional] 
**name** | **str** | Metadata descriptor name | [optional] 
**position** | **int** | Position of the descriptor | [optional] 
**entity_type** | **str** | Entity type | [optional] 

## Example

```python
from sometech.pykitsu._client.models.reorder_metadata_descriptors200_response_inner import ReorderMetadataDescriptors200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderMetadataDescriptors200ResponseInner from a JSON string
reorder_metadata_descriptors200_response_inner_instance = ReorderMetadataDescriptors200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ReorderMetadataDescriptors200ResponseInner.to_json())

# convert the object into a dict
reorder_metadata_descriptors200_response_inner_dict = reorder_metadata_descriptors200_response_inner_instance.to_dict()
# create an instance of ReorderMetadataDescriptors200ResponseInner from a dict
reorder_metadata_descriptors200_response_inner_from_dict = ReorderMetadataDescriptors200ResponseInner.from_dict(reorder_metadata_descriptors200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


