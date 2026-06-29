

# UpdateRegistryRecordStatus
<a name="API_UpdateRegistryRecordStatus"></a>

Updates the status of a registry record. Use this operation to approve, reject, or deprecate a registry record.

## Request Syntax
<a name="API_UpdateRegistryRecordStatus_RequestSyntax"></a>

```
PATCH /registries/{{registryId}}/records/{{recordId}}/status HTTP/1.1
Content-type: application/json

{
   "status": "{{string}}",
   "statusReason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRegistryRecordStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recordId](#API_UpdateRegistryRecordStatus_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecordStatus-request-uri-recordId"></a>
The identifier of the registry record to update the status for. You can specify either the Amazon Resource Name (ARN) or the ID of the record.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** [registryId](#API_UpdateRegistryRecordStatus_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecordStatus-request-uri-registryId"></a>
The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_UpdateRegistryRecordStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [status](#API_UpdateRegistryRecordStatus_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecordStatus-request-status"></a>
The target status for the registry record.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`   
Required: Yes

 ** [statusReason](#API_UpdateRegistryRecordStatus_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecordStatus-request-statusReason"></a>
The reason for the status change, such as why the record was approved or rejected.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_UpdateRegistryRecordStatus_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "recordArn": "string",
   "recordId": "string",
   "registryArn": "string",
   "status": "string",
   "statusReason": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateRegistryRecordStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [recordArn](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecordStatus-response-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}` 

 ** [recordId](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecordStatus-response-recordId"></a>
The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}` 

 ** [registryArn](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecordStatus-response-registryArn"></a>
The Amazon Resource Name (ARN) of the registry that contains the record.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [status](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecordStatus-response-status"></a>
The resulting status of the registry record.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED` 

 ** [statusReason](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecordStatus-response-statusReason"></a>
The reason for the status change.  
Type: String

 ** [updatedAt](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateRegistryRecordStatus-response-updatedAt"></a>
The timestamp when the record was last updated.  
Type: Timestamp

## Errors
<a name="API_UpdateRegistryRecordStatus_Errors"></a>

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
<a name="API_UpdateRegistryRecordStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecordStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecordStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecordStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecordStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecordStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecordStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecordStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecordStatus) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecordStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateRegistryRecordStatus) 