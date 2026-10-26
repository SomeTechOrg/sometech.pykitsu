# AddPersonToProductionTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_id** | **UUID** | Person unique identifier | 

## Example

```python
from sometech.pykitsu._client.models.add_person_to_production_team_request import AddPersonToProductionTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPersonToProductionTeamRequest from a JSON string
add_person_to_production_team_request_instance = AddPersonToProductionTeamRequest.from_json(json)
# print the JSON string representation of the object
print(AddPersonToProductionTeamRequest.to_json())

# convert the object into a dict
add_person_to_production_team_request_dict = add_person_to_production_team_request_instance.to_dict()
# create an instance of AddPersonToProductionTeamRequest from a dict
add_person_to_production_team_request_from_dict = AddPersonToProductionTeamRequest.from_dict(add_person_to_production_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


