# GetProductionDayOffs200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Day off unique identifier | [optional] 
**person_id** | **UUID** | Person unique identifier | [optional] 
**description** | **str** | Day off description | [optional] 
**var_date** | **date** | Day off start date | [optional] 
**end_date** | **date** | Day off end date | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_production_day_offs200_response_inner import GetProductionDayOffs200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductionDayOffs200ResponseInner from a JSON string
get_production_day_offs200_response_inner_instance = GetProductionDayOffs200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetProductionDayOffs200ResponseInner.to_json())

# convert the object into a dict
get_production_day_offs200_response_inner_dict = get_production_day_offs200_response_inner_instance.to_dict()
# create an instance of GetProductionDayOffs200ResponseInner from a dict
get_production_day_offs200_response_inner_from_dict = GetProductionDayOffs200ResponseInner.from_dict(get_production_day_offs200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


