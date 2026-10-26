# ImportOtioEdl201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_shots** | [**List[ImportOtioEdl201ResponseUpdatedShotsInner]**](ImportOtioEdl201ResponseUpdatedShotsInner.md) |  | [optional] 
**created_shots** | [**List[ImportOtioEdl201ResponseCreatedShotsInner]**](ImportOtioEdl201ResponseCreatedShotsInner.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_otio_edl201_response import ImportOtioEdl201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImportOtioEdl201Response from a JSON string
import_otio_edl201_response_instance = ImportOtioEdl201Response.from_json(json)
# print the JSON string representation of the object
print(ImportOtioEdl201Response.to_json())

# convert the object into a dict
import_otio_edl201_response_dict = import_otio_edl201_response_instance.to_dict()
# create an instance of ImportOtioEdl201Response from a dict
import_otio_edl201_response_from_dict = ImportOtioEdl201Response.from_dict(import_otio_edl201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


