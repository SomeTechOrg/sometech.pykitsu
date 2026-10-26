# GetDayOffGetDataPersonsPersonIdDayOffsDate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Day off unique identifier | [optional] 
**person_id** | **UUID** | Person unique identifier | [optional] 
**var_date** | **date** | Day off date | [optional] 
**type** | **str** | Day off type | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_day_off_get_data_persons_person_id_day_offs_date200_response import GetDayOffGetDataPersonsPersonIdDayOffsDate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDayOffGetDataPersonsPersonIdDayOffsDate200Response from a JSON string
get_day_off_get_data_persons_person_id_day_offs_date200_response_instance = GetDayOffGetDataPersonsPersonIdDayOffsDate200Response.from_json(json)
# print the JSON string representation of the object
print(GetDayOffGetDataPersonsPersonIdDayOffsDate200Response.to_json())

# convert the object into a dict
get_day_off_get_data_persons_person_id_day_offs_date200_response_dict = get_day_off_get_data_persons_person_id_day_offs_date200_response_instance.to_dict()
# create an instance of GetDayOffGetDataPersonsPersonIdDayOffsDate200Response from a dict
get_day_off_get_data_persons_person_id_day_offs_date200_response_from_dict = GetDayOffGetDataPersonsPersonIdDayOffsDate200Response.from_dict(get_day_off_get_data_persons_person_id_day_offs_date200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


