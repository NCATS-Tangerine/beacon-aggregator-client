# ServerConceptsQueryBeaconStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beacon** | **int** | Index number of beacon providing these concept details  | [optional] 
**status** | **int** | Http code status of beacon API - 200 means &#39;data ready&#39;, 102 means &#39;query in progress&#39;, other codes (e.g. 500) are server errors. Once a beacon has a &#39;200&#39; success code, then the /concepts/data  endpoint may be used to retrieve it.  | [optional] 
**discovered** | **int** | A count of how many items a beacon has returned. This number will not always be the same as the final number of results since we merge duplicate items.  | [optional] 
**processed** | **int** | A count of how many of the beacon responses have been processed and are ready for consumption.  | [optional] 
**count** | **int** | When a 200 status code is returned, this integer designates  the number of concepts matched by the query for the given beacon.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


