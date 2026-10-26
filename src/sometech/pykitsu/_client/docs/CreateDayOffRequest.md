# CreateDayOffRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**end_date** | **date** |  | 
**person_id** | **UUID** |  | 

## Example

```python
from sometech.pykitsu._client.models.create_day_off_request import CreateDayOffRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDayOffRequest from a JSON string
create_day_off_request_instance = CreateDayOffRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDayOffRequest.to_json())

# convert the object into a dict
create_day_off_request_dict = create_day_off_request_instance.to_dict()
# create an instance of CreateDayOffRequest from a dict
create_day_off_request_from_dict = CreateDayOffRequest.from_dict(create_day_off_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


