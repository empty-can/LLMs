

# AddDatasetExamples
<a name="API_AddDatasetExamples"></a>

 Adds examples to the dataset's DRAFT. All examples are validated against the dataset's schema type before any writes occur. If any example fails validation, the entire batch is rejected (all-or-nothing semantics). 

## Request Syntax
<a name="API_AddDatasetExamples_RequestSyntax"></a>

```
POST /datasets/{{datasetId}}/examples/add HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "source": { ... }
}
```

## URI Request Parameters
<a name="API_AddDatasetExamples_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_AddDatasetExamples_RequestSyntax) **   <a name="bedrockagentcorecontrol-AddDatasetExamples-request-uri-datasetId"></a>
 The unique identifier of the dataset to add examples to.   
Pattern: `[a-zA-Z0-9_-]{1,110}`   
Required: Yes

## Request Body
<a name="API_AddDatasetExamples_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_AddDatasetExamples_RequestSyntax) **   <a name="bedrockagentcorecontrol-AddDatasetExamples-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [source](#API_AddDatasetExamples_RequestSyntax) **   <a name="bedrockagentcorecontrol-AddDatasetExamples-request-source"></a>
 Source of examples to add. Provide either inline examples or an S3 URI pointing to a JSONL file.   
Type: [DataSourceType](API_DataSourceType.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_AddDatasetExamples_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "addedCount": number,
   "datasetArn": "string",
   "datasetId": "string",
   "exampleIds": [ "string" ],
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_AddDatasetExamples_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [addedCount](#API_AddDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-AddDatasetExamples-response-addedCount"></a>
 The number of examples added.   
Type: Long

 ** [datasetArn](#API_AddDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-AddDatasetExamples-response-datasetArn"></a>
 The Amazon Resource Name (ARN) of the dataset.   
Type: String  
Pattern: `arn:aws(-[a-z]+)*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:dataset/[a-zA-Z0-9_-]{1,110}` 

 ** [datasetId](#API_AddDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-AddDatasetExamples-response-datasetId"></a>
 The unique identifier of the dataset.   
Type: String  
Pattern: `[a-zA-Z0-9_-]{1,110}` 

 ** [exampleIds](#API_AddDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-AddDatasetExamples-response-exampleIds"></a>
 IDs of all added examples (auto-generated UUIDs).   
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[a-zA-Z0-9_.:-]+` 

 ** [status](#API_AddDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-AddDatasetExamples-response-status"></a>
 The current status of the dataset.   
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [updatedAt](#API_AddDatasetExamples_ResponseSyntax) **   <a name="bedrockagentcorecontrol-AddDatasetExamples-response-updatedAt"></a>
 The timestamp when the examples were added.   
Type: Timestamp

## Errors
<a name="API_AddDatasetExamples_Errors"></a>

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

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_AddDatasetExamples_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/AddDatasetExamples) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/AddDatasetExamples) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/AddDatasetExamples) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/AddDatasetExamples) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/AddDatasetExamples) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/AddDatasetExamples) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/AddDatasetExamples) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/AddDatasetExamples) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/AddDatasetExamples) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/AddDatasetExamples) 