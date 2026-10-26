# CreateOrganisationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**hours_by_day** | **float** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_organisation_request import CreateOrganisationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganisationRequest from a JSON string
create_organisation_request_instance = CreateOrganisationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganisationRequest.to_json())

# convert the object into a dict
create_organisation_request_dict = create_organisation_request_instance.to_dict()
# create an instance of CreateOrganisationRequest from a dict
create_organisation_request_from_dict = CreateOrganisationRequest.from_dict(create_organisation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


