# CreateDayOff201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**var_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**person_id** | **UUID** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_day_off201_response import CreateDayOff201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDayOff201Response from a JSON string
create_day_off201_response_instance = CreateDayOff201Response.from_json(json)
# print the JSON string representation of the object
print(CreateDayOff201Response.to_json())

# convert the object into a dict
create_day_off201_response_dict = create_day_off201_response_instance.to_dict()
# create an instance of CreateDayOff201Response from a dict
create_day_off201_response_from_dict = CreateDayOff201Response.from_dict(create_day_off201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


