# UpdateOrganisationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**hours_by_day** | **float** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_organisation_request import UpdateOrganisationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganisationRequest from a JSON string
update_organisation_request_instance = UpdateOrganisationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganisationRequest.to_json())

# convert the object into a dict
update_organisation_request_dict = update_organisation_request_instance.to_dict()
# create an instance of UpdateOrganisationRequest from a dict
update_organisation_request_from_dict = UpdateOrganisationRequest.from_dict(update_organisation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


