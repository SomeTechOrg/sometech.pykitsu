# OutputType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.output_type import OutputType

# TODO update the JSON string below
json = "{}"
# create an instance of OutputType from a JSON string
output_type_instance = OutputType.from_json(json)
# print the JSON string representation of the object
print(OutputType.to_json())

# convert the object into a dict
output_type_dict = output_type_instance.to_dict()
# create an instance of OutputType from a dict
output_type_from_dict = OutputType.from_dict(output_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


