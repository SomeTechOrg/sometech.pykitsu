# ReplyToComment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Reply unique identifier | [optional] 
**comment_id** | **UUID** | Parent comment identifier | [optional] 
**text** | **str** | Reply text content | [optional] 
**person_id** | **UUID** | Person identifier who made the reply | [optional] 
**created_at** | **datetime** | Creation timestamp | [optional] 

## Example

```python
from sometech.pykitsu._client.models.reply_to_comment200_response import ReplyToComment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReplyToComment200Response from a JSON string
reply_to_comment200_response_instance = ReplyToComment200Response.from_json(json)
# print the JSON string representation of the object
print(ReplyToComment200Response.to_json())

# convert the object into a dict
reply_to_comment200_response_dict = reply_to_comment200_response_instance.to_dict()
# create an instance of ReplyToComment200Response from a dict
reply_to_comment200_response_from_dict = ReplyToComment200Response.from_dict(reply_to_comment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


