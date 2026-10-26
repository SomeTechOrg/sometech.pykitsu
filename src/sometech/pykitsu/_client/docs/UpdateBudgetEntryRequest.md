# UpdateBudgetEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**department_id** | **UUID** | Department unique identifier | [optional] 
**person_id** | **UUID** | Person unique identifier | [optional] 
**start_date** | **date** | Budget entry start date | [optional] 
**months_duration** | **int** | Budget entry duration in months | [optional] 
**daily_salary** | **float** | Daily salary amount | [optional] 
**position** | **str** | Position name | [optional] 
**seniority** | **str** | Seniority level | [optional] 
**exceptions** | **object** | Map of amount exceptions. Key is the date and value is the amount | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_budget_entry_request import UpdateBudgetEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBudgetEntryRequest from a JSON string
update_budget_entry_request_instance = UpdateBudgetEntryRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateBudgetEntryRequest.to_json())

# convert the object into a dict
update_budget_entry_request_dict = update_budget_entry_request_instance.to_dict()
# create an instance of UpdateBudgetEntryRequest from a dict
update_budget_entry_request_from_dict = UpdateBudgetEntryRequest.from_dict(update_budget_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


