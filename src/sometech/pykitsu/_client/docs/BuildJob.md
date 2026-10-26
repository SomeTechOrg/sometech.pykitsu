# BuildJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of build job (running, failed, succeeded) | [optional] 
**job_type** | **str** | Type of build job (archive, movie) | [optional] 
**ended_at** | **datetime** |  | [optional] 
**playlist_id** | **UUID** | Playlist ID | [optional] 

## Example

```python
from sometech.pykitsu._client.models.build_job import BuildJob

# TODO update the JSON string below
json = "{}"
# create an instance of BuildJob from a JSON string
build_job_instance = BuildJob.from_json(json)
# print the JSON string representation of the object
print(BuildJob.to_json())

# convert the object into a dict
build_job_dict = build_job_instance.to_dict()
# create an instance of BuildJob from a dict
build_job_from_dict = BuildJob.from_dict(build_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


