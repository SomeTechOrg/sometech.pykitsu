# UpdateSalaryScale200Response


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
from sometech.pykitsu._client.models.update_salary_scale200_response import UpdateSalaryScale200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSalaryScale200Response from a JSON string
update_salary_scale200_response_instance = UpdateSalaryScale200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateSalaryScale200Response.to_json())

# convert the object into a dict
update_salary_scale200_response_dict = update_salary_scale200_response_instance.to_dict()
# create an instance of UpdateSalaryScale200Response from a dict
update_salary_scale200_response_from_dict = UpdateSalaryScale200Response.from_dict(update_salary_scale200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


