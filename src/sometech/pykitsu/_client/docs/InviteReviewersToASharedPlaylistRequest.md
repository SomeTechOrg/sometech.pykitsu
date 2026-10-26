# InviteReviewersToASharedPlaylistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** |  | [optional] 
**person_ids** | **List[UUID]** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from sometech.pykitsu._client.models.invite_reviewers_to_a_shared_playlist_request import InviteReviewersToASharedPlaylistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InviteReviewersToASharedPlaylistRequest from a JSON string
invite_reviewers_to_a_shared_playlist_request_instance = InviteReviewersToASharedPlaylistRequest.from_json(json)
# print the JSON string representation of the object
print(InviteReviewersToASharedPlaylistRequest.to_json())

# convert the object into a dict
invite_reviewers_to_a_shared_playlist_request_dict = invite_reviewers_to_a_shared_playlist_request_instance.to_dict()
# create an instance of InviteReviewersToASharedPlaylistRequest from a dict
invite_reviewers_to_a_shared_playlist_request_from_dict = InviteReviewersToASharedPlaylistRequest.from_dict(invite_reviewers_to_a_shared_playlist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


