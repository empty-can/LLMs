

# DeletePolicy
<a name="API_DeletePolicy"></a>

Deletes an existing policy from the AgentCore Policy system. Once deleted, the policy can no longer be used for agent behavior control and all references to it become invalid. This is an asynchronous operation. Use the `GetPolicy` operation to poll the `status` field to track completion.

## Request Syntax
<a name="API_DeletePolicy_RequestSyntax"></a>

```
DELETE /policy-engines/{{policyEngineId}}/policies/{{policyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyEngineId](#API_DeletePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-request-uri-policyEngineId"></a>
The identifier of the policy engine that manages the policy to be deleted. This ensures the policy is deleted from the correct policy engine context.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** [policyId](#API_DeletePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-request-uri-policyId"></a>
The unique identifier of the policy to be deleted. This must be a valid policy ID that exists within the specified policy engine.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

## Request Body
<a name="API_DeletePolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePolicy_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": "string",
   "definition": { ... },
   "description": "string",
   "enforcementMode": "string",
   "name": "string",
   "policyArn": "string",
   "policyEngineId": "string",
   "policyId": "string",
   "status": "string",
   "statusReasons": [ "string" ],
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_DeletePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_DeletePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-response-createdAt"></a>
The timestamp when the deleted policy was originally created.  
Type: Timestamp

 ** [definition](#API_DeletePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-response-definition"></a>
Represents the definition structure for policies within the AgentCore Policy system. This structure encapsulates different policy formats and languages that can be used to define access control rules.  
Type: [PolicyDefinition](API_PolicyDefinition.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [description](#API_DeletePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-response-description"></a>
The human-readable description of the deleted policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [enforcementMode](#API_DeletePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-response-enforcementMode"></a>
The enforcement mode of the deleted policy.  
Type: String  
Valid Values: `ACTIVE | LOG_ONLY` 

 ** [name](#API_DeletePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-response-name"></a>
The customer-assigned name of the deleted policy. This confirms which policy was successfully removed from the system and matches the name that was originally assigned during policy creation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*` 

 ** [policyArn](#API_DeletePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-response-policyArn"></a>
The Amazon Resource Name (ARN) of the deleted policy. This globally unique identifier confirms which policy resource was successfully removed.  
Type: String  
Length Constraints: Minimum length of 96. Maximum length of 203.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}` 

 ** [policyEngineId](#API_DeletePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-response-policyEngineId"></a>
The identifier of the policy engine from which the policy was deleted. This confirms the policy engine context for the deletion operation.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [policyId](#API_DeletePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-response-policyId"></a>
The unique identifier of the policy being deleted. This confirms which policy the deletion operation targets.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [status](#API_DeletePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-response-status"></a>
The status of the policy deletion operation. This provides information about any issues that occurred during the deletion process.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [statusReasons](#API_DeletePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-response-statusReasons"></a>
Additional information about the deletion status. This provides details about the deletion process or any issues that may have occurred.  
Type: Array of strings

 ** [updatedAt](#API_DeletePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeletePolicy-response-updatedAt"></a>
The timestamp when the deleted policy was last modified before deletion. This tracks the final state of the policy before it was removed from the system.  
Type: Timestamp

## Errors
<a name="API_DeletePolicy_Errors"></a>

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
<a name="API_DeletePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeletePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeletePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeletePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeletePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeletePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeletePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeletePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeletePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeletePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeletePolicy) 