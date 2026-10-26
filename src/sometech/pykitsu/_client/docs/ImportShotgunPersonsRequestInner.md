# ImportShotgunPersonsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Shotgun ID of the person | [optional] 
**firstname** | **str** | First name | [optional] 
**lastname** | **str** | Last name | [optional] 
**email** | **str** | Email address | [optional] 
**login** | **str** | Desktop login | [optional] 
**sg_status_list** | **str** | Status list | [optional] 
**permission_rule_set** | [**ImportShotgunPersonsRequestInnerPermissionRuleSet**](ImportShotgunPersonsRequestInnerPermissionRuleSet.md) |  | [optional] 
**department** | [**ImportShotgunPersonsRequestInnerDepartment**](ImportShotgunPersonsRequestInnerDepartment.md) |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.import_shotgun_persons_request_inner import ImportShotgunPersonsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ImportShotgunPersonsRequestInner from a JSON string
import_shotgun_persons_request_inner_instance = ImportShotgunPersonsRequestInner.from_json(json)
# print the JSON string representation of the object
print(ImportShotgunPersonsRequestInner.to_json())

# convert the object into a dict
import_shotgun_persons_request_inner_dict = import_shotgun_persons_request_inner_instance.to_dict()
# create an instance of ImportShotgunPersonsRequestInner from a dict
import_shotgun_persons_request_inner_from_dict = ImportShotgunPersonsRequestInner.from_dict(import_shotgun_persons_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


