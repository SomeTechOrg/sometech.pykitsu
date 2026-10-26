# Studio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of studio | [optional] 
**color** | **str** | Color of studio | [optional] 
**archived** | **bool** | True if the studio is archived else False | [optional] 

## Example

```python
from sometech.pykitsu._client.models.studio import Studio

# TODO update the JSON string below
json = "{}"
# create an instance of Studio from a JSON string
studio_instance = Studio.from_json(json)
# print the JSON string representation of the object
print(Studio.to_json())

# convert the object into a dict
studio_dict = studio_instance.to_dict()
# create an instance of Studio from a dict
studio_from_dict = Studio.from_dict(studio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


