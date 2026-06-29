

# DeleteDatasetExamples
<a name="API_DeleteDatasetExamples"></a>

 Deletes specific examples by ID from DRAFT. All example IDs are validated before any deletes occur. If any ID does not exist in DRAFT, the entire batch is rejected (all-or-nothing semantics). 

## Request Syntax
<a name="API_DeleteDatasetExamples_RequestSyntax"></a>

```
POST /datasets/{{datasetId}}/examples/delete HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "exampleIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DeleteDatasetExamples_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_DeleteDatasetExamples_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteDatasetExamples-request-uri-datasetId"></a>
 The unique identifier of the dataset.   
Pattern: `[a-zA-Z0-9_-]{1,110}`   
Required: Yes

## Request Body
<a name="API_DeleteDatasetExamples_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_DeleteDatasetExamples_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteDatasetExamples-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [exampleIds](#API_DeleteDatasetExamples_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteDatasetExamples-request-exampleIds"></a>
 The IDs of the examples to delete.   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[a-zA-Z0-9_.:-]+`   
Required: Yes

## Response Syntax
<a name="API_DeleteDatasetExamples_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "datasetArn": "string",
   "datasetId": "string",
   "deletedCount": number,
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_DeleteDatasetExamples_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [datasetArn](#API_DeleteDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteDatasetExamples-response-datasetArn"></a>
 The Amazon Resource Name (ARN) of the dataset.   
Type: String  
Pattern: `arn:aws(-[a-z]+)*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:dataset/[a-zA-Z0-9_-]{1,110}` 

 ** [datasetId](#API_DeleteDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteDatasetExamples-response-datasetId"></a>
 The unique identifier of the dataset.   
Type: String  
Pattern: `[a-zA-Z0-9_-]{1,110}` 

 ** [deletedCount](#API_DeleteDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteDatasetExamples-response-deletedCount"></a>
 The number of examples deleted.   
Type: Long

 ** [status](#API_DeleteDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteDatasetExamples-response-status"></a>
 The current status of the dataset.   
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [updatedAt](#API_DeleteDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteDatasetExamples-response-updatedAt"></a>
 The timestamp when the examples were deleted.   
Type: Timestamp

## Errors
<a name="API_DeleteDatasetExamples_Errors"></a>

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
<a name="API_DeleteDatasetExamples_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeleteDatasetExamples) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeleteDatasetExamples) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeleteDatasetExamples) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeleteDatasetExamples) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeleteDatasetExamples) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeleteDatasetExamples) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeleteDatasetExamples) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeleteDatasetExamples) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeleteDatasetExamples) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeleteDatasetExamples) 