# RemoveShotgunPersonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the person to remove | 

## Example

```python
from sometech.pykitsu._client.models.remove_shotgun_person_request import RemoveShotgunPersonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveShotgunPersonRequest from a JSON string
remove_shotgun_person_request_instance = RemoveShotgunPersonRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveShotgunPersonRequest.to_json())

# convert the object into a dict
remove_shotgun_person_request_dict = remove_shotgun_person_request_instance.to_dict()
# create an instance of RemoveShotgunPersonRequest from a dict
remove_shotgun_person_request_from_dict = RemoveShotgunPersonRequest.from_dict(remove_shotgun_person_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


