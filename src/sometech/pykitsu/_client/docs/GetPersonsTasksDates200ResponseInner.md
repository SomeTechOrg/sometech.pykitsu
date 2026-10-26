# GetPersonsTasksDates200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_id** | **UUID** |  | [optional] 
**first_start_date** | **date** |  | [optional] 
**last_end_date** | **date** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.get_persons_tasks_dates200_response_inner import GetPersonsTasksDates200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPersonsTasksDates200ResponseInner from a JSON string
get_persons_tasks_dates200_response_inner_instance = GetPersonsTasksDates200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetPersonsTasksDates200ResponseInner.to_json())

# convert the object into a dict
get_persons_tasks_dates200_response_inner_dict = get_persons_tasks_dates200_response_inner_instance.to_dict()
# create an instance of GetPersonsTasksDates200ResponseInner from a dict
get_persons_tasks_dates200_response_inner_from_dict = GetPersonsTasksDates200ResponseInner.from_dict(get_persons_tasks_dates200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


