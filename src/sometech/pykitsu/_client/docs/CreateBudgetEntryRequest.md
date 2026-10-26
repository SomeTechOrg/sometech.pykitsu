# CreateBudgetEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**department_id** | **UUID** | Department unique identifier | 
**person_id** | **UUID** | Person unique identifier | [optional] 
**start_date** | **date** | Budget entry start date | [optional] 
**months_duration** | **int** | Budget entry duration in months | [optional] 
**daily_salary** | **float** | Daily salary amount | [optional] 
**position** | **str** | Position name | [optional] 
**seniority** | **str** | Seniority level | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_budget_entry_request import CreateBudgetEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBudgetEntryRequest from a JSON string
create_budget_entry_request_instance = CreateBudgetEntryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBudgetEntryRequest.to_json())

# convert the object into a dict
create_budget_entry_request_dict = create_budget_entry_request_instance.to_dict()
# create an instance of CreateBudgetEntryRequest from a dict
create_budget_entry_request_from_dict = CreateBudgetEntryRequest.from_dict(create_budget_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


