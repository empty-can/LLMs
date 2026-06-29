

# ListDatasetVersions
<a name="API_ListDatasetVersions"></a>

 Lists all published versions of a dataset, sorted by version number descending (newest first). Does not include the DRAFT working copy. 

## Request Syntax
<a name="API_ListDatasetVersions_RequestSyntax"></a>

```
GET /datasets/{{datasetId}}/versions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDatasetVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_ListDatasetVersions_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetVersions-request-uri-datasetId"></a>
 The unique identifier of the dataset.   
Pattern: `[a-zA-Z0-9_-]{1,110}`   
Required: Yes

 ** [maxResults](#API_ListDatasetVersions_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetVersions-request-uri-maxResults"></a>
 The maximum number of versions to return per page.   
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListDatasetVersions_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetVersions-request-uri-nextToken"></a>
 The token for the next page of results. 

## Request Body
<a name="API_ListDatasetVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDatasetVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "versions": [ 
      { 
         "createdAt": number,
         "datasetVersion": "string",
         "exampleCount": number
      }
   ]
}
```

## Response Elements
<a name="API_ListDatasetVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListDatasetVersions_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetVersions-response-nextToken"></a>
 The token for the next page of results, or null if there are no more results.   
Type: String

 ** [versions](#API_ListDatasetVersions_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetVersions-response-versions"></a>
 The list of published dataset versions.   
Type: Array of [DatasetVersionSummary](API_DatasetVersionSummary.md) objects

## Errors
<a name="API_ListDatasetVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_ListDatasetVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListDatasetVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListDatasetVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListDatasetVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListDatasetVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListDatasetVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListDatasetVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListDatasetVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListDatasetVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListDatasetVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListDatasetVersions) 