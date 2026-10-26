# Organisation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of organisation | [optional] 
**hours_by_day** | **float** |  | [optional] 
**has_avatar** | **bool** | True if the organisation has an avatar, False otherwise | [optional] [default to False]
**use_original_file_name** | **bool** | True if the organisation uses original file names, False otherwise | [optional] [default to False]
**timesheets_locked** | **bool** | True if the organisation&#39;s timesheets are locked, False otherwise | [optional] [default to False]
**hd_by_default** | **bool** |  | [optional] [default to False]
**chat_token_slack** | **str** |  | [optional] 
**chat_webhook_mattermost** | **str** |  | [optional] 
**chat_token_discord** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.organisation import Organisation

# TODO update the JSON string below
json = "{}"
# create an instance of Organisation from a JSON string
organisation_instance = Organisation.from_json(json)
# print the JSON string representation of the object
print(Organisation.to_json())

# convert the object into a dict
organisation_dict = organisation_instance.to_dict()
# create an instance of Organisation from a dict
organisation_from_dict = Organisation.from_dict(organisation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


