# UpdateSalaryScaleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_salary_scale_request import UpdateSalaryScaleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSalaryScaleRequest from a JSON string
update_salary_scale_request_instance = UpdateSalaryScaleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSalaryScaleRequest.to_json())

# convert the object into a dict
update_salary_scale_request_dict = update_salary_scale_request_instance.to_dict()
# create an instance of UpdateSalaryScaleRequest from a dict
update_salary_scale_request_from_dict = UpdateSalaryScaleRequest.from_dict(update_salary_scale_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


