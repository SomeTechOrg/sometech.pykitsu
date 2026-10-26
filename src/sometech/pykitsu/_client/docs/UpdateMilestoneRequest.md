# UpdateMilestoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**var_date** | **date** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.update_milestone_request import UpdateMilestoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMilestoneRequest from a JSON string
update_milestone_request_instance = UpdateMilestoneRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMilestoneRequest.to_json())

# convert the object into a dict
update_milestone_request_dict = update_milestone_request_instance.to_dict()
# create an instance of UpdateMilestoneRequest from a dict
update_milestone_request_from_dict = UpdateMilestoneRequest.from_dict(update_milestone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


