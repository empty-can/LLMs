

# SubmitRegistryRecordForApproval
<a name="API_SubmitRegistryRecordForApproval"></a>

Submits a registry record for approval. This transitions the record from `DRAFT` status to `PENDING_APPROVAL` status. If the registry has auto-approval enabled, the record is automatically approved.

## Request Syntax
<a name="API_SubmitRegistryRecordForApproval_RequestSyntax"></a>

```
POST /registries/{{registryId}}/records/{{recordId}}/submit-for-approval HTTP/1.1
```

## URI Request Parameters
<a name="API_SubmitRegistryRecordForApproval_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recordId](#API_SubmitRegistryRecordForApproval_RequestSyntax) **   <a name="bedrockagentcorecontrol-SubmitRegistryRecordForApproval-request-uri-recordId"></a>
The identifier of the registry record to submit for approval. You can specify either the Amazon Resource Name (ARN) or the ID of the record.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** [registryId](#API_SubmitRegistryRecordForApproval_RequestSyntax) **   <a name="bedrockagentcorecontrol-SubmitRegistryRecordForApproval-request-uri-registryId"></a>
The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_SubmitRegistryRecordForApproval_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_SubmitRegistryRecordForApproval_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "recordArn": "string",
   "recordId": "string",
   "registryArn": "string",
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_SubmitRegistryRecordForApproval_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [recordArn](#API_SubmitRegistryRecordForApproval_ResponseSyntax) **   <a name="bedrockagentcorecontrol-SubmitRegistryRecordForApproval-response-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}` 

 ** [recordId](#API_SubmitRegistryRecordForApproval_ResponseSyntax) **   <a name="bedrockagentcorecontrol-SubmitRegistryRecordForApproval-response-recordId"></a>
The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}` 

 ** [registryArn](#API_SubmitRegistryRecordForApproval_ResponseSyntax) **   <a name="bedrockagentcorecontrol-SubmitRegistryRecordForApproval-response-registryArn"></a>
The Amazon Resource Name (ARN) of the registry that contains the record.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [status](#API_SubmitRegistryRecordForApproval_ResponseSyntax) **   <a name="bedrockagentcorecontrol-SubmitRegistryRecordForApproval-response-status"></a>
The resulting status of the registry record after submission.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED` 

 ** [updatedAt](#API_SubmitRegistryRecordForApproval_ResponseSyntax) **   <a name="bedrockagentcorecontrol-SubmitRegistryRecordForApproval-response-updatedAt"></a>
The timestamp when the record was last updated.  
Type: Timestamp

## Errors
<a name="API_SubmitRegistryRecordForApproval_Errors"></a>

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
<a name="API_SubmitRegistryRecordForApproval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/SubmitRegistryRecordForApproval) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/SubmitRegistryRecordForApproval) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SubmitRegistryRecordForApproval) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/SubmitRegistryRecordForApproval) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SubmitRegistryRecordForApproval) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/SubmitRegistryRecordForApproval) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/SubmitRegistryRecordForApproval) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/SubmitRegistryRecordForApproval) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/SubmitRegistryRecordForApproval) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SubmitRegistryRecordForApproval) 