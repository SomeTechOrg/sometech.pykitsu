# Person


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** | Serve as login | [optional] 
**phone** | **str** |  | [optional] 
**active** | **bool** | True if the person is still in the studio, False otherwise | [optional] 
**last_presence** | **date** | Last time the person worked for the studio | [optional] 
**password** | **bytes** |  | [optional] 
**desktop_login** | **str** | Login used on desktop | [optional] 
**shotgun_id** | **int** | Used for synchronization with a Shotgun instance | [optional] 
**timezone** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**data** | **str** | Free JSON field to add metadata | [optional] 
**role** | **str** |  | [optional] [default to 'user']
**has_avatar** | **bool** | True if user has an avatar, False otherwise | [optional] [default to False]
**notifications_enabled** | **bool** |  | [optional] 
**notifications_slack_enabled** | **bool** |  | [optional] 
**notifications_slack_userid** | **str** |  | [optional] 
**notifications_mattermost_enabled** | **bool** |  | [optional] 
**notifications_mattermost_userid** | **str** |  | [optional] 
**notifications_discord_enabled** | **bool** |  | [optional] 
**notifications_discord_userid** | **str** |  | [optional] 
**id** | **UUID** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print(Person.to_json())

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_from_dict = Person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


