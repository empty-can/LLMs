

# ListDatasetExamples
<a name="API_ListDatasetExamples"></a>

 Returns paginated examples from the dataset. The server embeds the resolved version in the pagination token. Once pagination begins, all subsequent pages are pinned to that version regardless of concurrent mutations. 

## Request Syntax
<a name="API_ListDatasetExamples_RequestSyntax"></a>

```
GET /datasets/{{datasetId}}/examples?datasetVersion={{datasetVersion}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDatasetExamples_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_ListDatasetExamples_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetExamples-request-uri-datasetId"></a>
 The unique identifier of the dataset.   
Pattern: `[a-zA-Z0-9_-]{1,110}`   
Required: Yes

 ** [datasetVersion](#API_ListDatasetExamples_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetExamples-request-uri-datasetVersion"></a>
 Version to paginate: "DRAFT" or a version number. Defaults to DRAFT if absent. Only used on the first request; for subsequent pages, the version is extracted from the pagination token.   
Pattern: `(DRAFT|[0-9]+)` 

 ** [maxResults](#API_ListDatasetExamples_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetExamples-request-uri-maxResults"></a>
 Maximum number of examples to return per page.   
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListDatasetExamples_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetExamples-request-uri-nextToken"></a>
 The token for the next page of results.   
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Request Body
<a name="API_ListDatasetExamples_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDatasetExamples_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasetArn": "string",
   "datasetId": "string",
   "datasetVersion": "string",
   "examples": [ JSON value ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDatasetExamples_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasetArn](#API_ListDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetExamples-response-datasetArn"></a>
 The Amazon Resource Name (ARN) of the dataset.   
Type: String  
Pattern: `arn:aws(-[a-z]+)*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:dataset/[a-zA-Z0-9_-]{1,110}` 

 ** [datasetId](#API_ListDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetExamples-response-datasetId"></a>
 The unique identifier of the dataset.   
Type: String  
Pattern: `[a-zA-Z0-9_-]{1,110}` 

 ** [datasetVersion](#API_ListDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetExamples-response-datasetVersion"></a>
 The version returned.   
Type: String  
Pattern: `(DRAFT|[0-9]+)` 

 ** [examples](#API_ListDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetExamples-response-examples"></a>
 Paginated example content. Each element is a JSON object containing at least an `exampleId` field plus the schema-specific content fields.   
Type: Array of JSON values

 ** [nextToken](#API_ListDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListDatasetExamples-response-nextToken"></a>
 The token for the next page of results, or null if there are no more results.   
Type: String

## Errors
<a name="API_ListDatasetExamples_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

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
<a name="API_ListDatasetExamples_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListDatasetExamples) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListDatasetExamples) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListDatasetExamples) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListDatasetExamples) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListDatasetExamples) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListDatasetExamples) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListDatasetExamples) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListDatasetExamples) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListDatasetExamples) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListDatasetExamples) 