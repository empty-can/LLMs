

# DeletePolicyEngine
<a name="API_DeletePolicyEngine"></a>

Deletes an existing policy engine from the AgentCore Policy system. The policy engine must not have any associated policies before deletion. Once deleted, the policy engine and all its configurations become unavailable for policy management and evaluation. This is an asynchronous operation. Use the `GetPolicyEngine` operation to poll the `status` field to track completion.

## Request Syntax
<a name="API_DeletePolicyEngine_RequestSyntax"></a>

```
DELETE /policy-engines/{{policyEngineId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePolicyEngine_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyEngineId](#API_DeletePolicyEngine_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicyEngine-request-uri-policyEngineId"></a>
The unique identifier of the policy engine to be deleted. This must be a valid policy engine ID that exists within the account.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

## Request Body
<a name="API_DeletePolicyEngine_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePolicyEngine_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": "string",
   "description": "string",
   "encryptionKeyArn": "string",
   "name": "string",
   "policyEngineArn": "string",
   "policyEngineId": "string",
   "status": "string",
   "statusReasons": [ "string" ],
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_DeletePolicyEngine_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_DeletePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicyEngine-response-createdAt"></a>
The timestamp when the deleted policy engine was originally created.  
Type: Timestamp

 ** [description](#API_DeletePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicyEngine-response-description"></a>
The human-readable description of the deleted policy engine.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [encryptionKeyArn](#API_DeletePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicyEngine-response-encryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the policy engine data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [name](#API_DeletePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicyEngine-response-name"></a>
The customer-assigned name of the deleted policy engine.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*` 

 ** [policyEngineArn](#API_DeletePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicyEngine-response-policyEngineArn"></a>
The Amazon Resource Name (ARN) of the deleted policy engine. This globally unique identifier confirms which policy engine resource was successfully removed.  
Type: String  
Length Constraints: Minimum length of 76. Maximum length of 136.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}` 

 ** [policyEngineId](#API_DeletePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicyEngine-response-policyEngineId"></a>
The unique identifier of the policy engine being deleted. This confirms which policy engine the deletion operation targets.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [status](#API_DeletePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicyEngine-response-status"></a>
The status of the policy engine deletion operation. This provides status about any issues that occurred during the deletion process.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [statusReasons](#API_DeletePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicyEngine-response-statusReasons"></a>
Additional information about the deletion status. This provides details about the deletion process or any issues that may have occurred.  
Type: Array of strings

 ** [updatedAt](#API_DeletePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicyEngine-response-updatedAt"></a>
The timestamp when the deleted policy engine was last modified before deletion. This tracks the final state of the policy engine before it was removed from the system.  
Type: Timestamp

## Errors
<a name="API_DeletePolicyEngine_Errors"></a>

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
<a name="API_DeletePolicyEngine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeletePolicyEngine) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeletePolicyEngine) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeletePolicyEngine) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeletePolicyEngine) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeletePolicyEngine) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeletePolicyEngine) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeletePolicyEngine) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeletePolicyEngine) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeletePolicyEngine) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeletePolicyEngine) 