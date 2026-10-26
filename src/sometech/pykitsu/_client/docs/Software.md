# Software


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of software | [optional] 
**short_name** | **str** | Short name of software | [optional] 
**file_extension** | **str** | Main extension used for this software&#39;s files | [optional] 
**secondary_extensions** | **str** | Other extensions used for this software&#39;s files | [optional] 

## Example

```python
from sometech.pykitsu._client.models.software import Software

# TODO update the JSON string below
json = "{}"
# create an instance of Software from a JSON string
software_instance = Software.from_json(json)
# print the JSON string representation of the object
print(Software.to_json())

# convert the object into a dict
software_dict = software_instance.to_dict()
# create an instance of Software from a dict
software_from_dict = Software.from_dict(software_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


