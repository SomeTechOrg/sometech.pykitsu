# GetProductionTeam200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Person unique identifier | [optional] 
**first_name** | **str** | Person first name | [optional] 
**last_name** | **str** | Person last name | [optional] 
**email** | **str** | Person email address | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_production_team200_response_inner import GetProductionTeam200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductionTeam200ResponseInner from a JSON string
get_production_team200_response_inner_instance = GetProductionTeam200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProductionTeam200ResponseInner.to_json())

# convert the object into a dict
get_production_team200_response_inner_dict = get_production_team200_response_inner_instance.to_dict()
# create an instance of GetProductionTeam200ResponseInner from a dict
get_production_team200_response_inner_from_dict = GetProductionTeam200ResponseInner.from_dict(get_production_team200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


