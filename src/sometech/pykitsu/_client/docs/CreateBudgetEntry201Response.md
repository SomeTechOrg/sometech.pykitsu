# CreateBudgetEntry201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Budget entry unique identifier | [optional] 
**department_id** | **UUID** | Department unique identifier | [optional] 

## Example

```python
from sometech.pykitsu._client.models.create_budget_entry201_response import CreateBudgetEntry201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBudgetEntry201Response from a JSON string
create_budget_entry201_response_instance = CreateBudgetEntry201Response.from_json(json)
# print the JSON string representation of the object
print(CreateBudgetEntry201Response.to_json())

# convert the object into a dict
create_budget_entry201_response_dict = create_budget_entry201_response_instance.to_dict()
# create an instance of CreateBudgetEntry201Response from a dict
create_budget_entry201_response_from_dict = CreateBudgetEntry201Response.from_dict(create_budget_entry201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


