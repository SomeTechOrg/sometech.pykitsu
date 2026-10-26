# CreateAssetInstancePostDataAssetInstancesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **UUID** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_asset_instance_post_data_asset_instances_request import CreateAssetInstancePostDataAssetInstancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetInstancePostDataAssetInstancesRequest from a JSON string
create_asset_instance_post_data_asset_instances_request_instance = CreateAssetInstancePostDataAssetInstancesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAssetInstancePostDataAssetInstancesRequest.to_json())

# convert the object into a dict
create_asset_instance_post_data_asset_instances_request_dict = create_asset_instance_post_data_asset_instances_request_instance.to_dict()
# create an instance of CreateAssetInstancePostDataAssetInstancesRequest from a dict
create_asset_instance_post_data_asset_instances_request_from_dict = CreateAssetInstancePostDataAssetInstancesRequest.from_dict(create_asset_instance_post_data_asset_instances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


