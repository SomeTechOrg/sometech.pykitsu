# AddPersonToProductionTeam201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Project unique identifier | [optional] 
**name** | **str** | Project name | [optional] 

## Example

```python
from sometech.pykitsu._client.models.add_person_to_production_team201_response import AddPersonToProductionTeam201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddPersonToProductionTeam201Response from a JSON string
add_person_to_production_team201_response_instance = AddPersonToProductionTeam201Response.from_json(json)
# print the JSON string representation of the object
print(AddPersonToProductionTeam201Response.to_json())

# convert the object into a dict
add_person_to_production_team201_response_dict = add_person_to_production_team201_response_instance.to_dict()
# create an instance of AddPersonToProductionTeam201Response from a dict
add_person_to_production_team201_response_from_dict = AddPersonToProductionTeam201Response.from_dict(add_person_to_production_team201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


