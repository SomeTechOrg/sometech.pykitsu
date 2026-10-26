# GetSalaryScale200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**department_id** | **UUID** |  | [optional] 
**position** | **str** |  | [optional] 
**seniority** | **str** |  | [optional] 
**rate** | **float** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_salary_scale200_response import GetSalaryScale200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSalaryScale200Response from a JSON string
get_salary_scale200_response_instance = GetSalaryScale200Response.from_json(json)
# print the JSON string representation of the object
print(GetSalaryScale200Response.to_json())

# convert the object into a dict
get_salary_scale200_response_dict = get_salary_scale200_response_instance.to_dict()
# create an instance of GetSalaryScale200Response from a dict
get_salary_scale200_response_from_dict = GetSalaryScale200Response.from_dict(get_salary_scale200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


