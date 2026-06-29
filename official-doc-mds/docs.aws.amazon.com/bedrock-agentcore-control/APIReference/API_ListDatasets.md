

# ListDatasets
<a name="API_ListDatasets"></a>

 Lists all datasets in the caller's account, paginated. 

## Request Syntax
<a name="API_ListDatasets_RequestSyntax"></a>

```
GET /datasets?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDatasets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListDatasets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasets-request-uri-maxResults"></a>
 The maximum number of datasets to return per page.   
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListDatasets_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasets-request-uri-nextToken"></a>
 The token for the next page of results.   
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Request Body
<a name="API_ListDatasets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDatasets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasets": [ 
      { 
         "createdAt": number,
         "datasetArn": "string",
         "datasetId": "string",
         "datasetName": "string",
         "description": "string",
         "draftStatus": "string",
         "exampleCount": number,
         "schemaType": "string",
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDatasets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasets](#API_ListDatasets_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListDatasets-response-datasets"></a>
 The list of datasets.   
Type: Array of [DatasetSummary](API_DatasetSummary.md) objects

 ** [nextToken](#API_ListDatasets_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListDatasets-response-nextToken"></a>
 The token for the next page of results, or null if there are no more results.   
Type: String

## Errors
<a name="API_ListDatasets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_ListDatasets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListDatasets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListDatasets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListDatasets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListDatasets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListDatasets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListDatasets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListDatasets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListDatasets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListDatasets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListDatasets) 