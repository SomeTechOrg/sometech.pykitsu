# AcknowledgeComment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Comment unique identifier | [optional] 
**acknowledged** | **bool** | Whether the comment is acknowledged | [optional] 

## Example

```python
from sometech.pykitsu._client.models.acknowledge_comment200_response import AcknowledgeComment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AcknowledgeComment200Response from a JSON string
acknowledge_comment200_response_instance = AcknowledgeComment200Response.from_json(json)
# print the JSON string representation of the object
print(AcknowledgeComment200Response.to_json())

# convert the object into a dict
acknowledge_comment200_response_dict = acknowledge_comment200_response_instance.to_dict()
# create an instance of AcknowledgeComment200Response from a dict
acknowledge_comment200_response_from_dict = AcknowledgeComment200Response.from_dict(acknowledge_comment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


