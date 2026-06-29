

# CreatePolicyEngine
<a name="API_CreatePolicyEngine"></a>

Creates a new policy engine within the AgentCore Policy system. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with Gateways (each Gateway can be associated with at most one policy engine, but multiple Gateways can be associated with the same engine), the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies. This is an asynchronous operation. Use the [GetPolicyEngine](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicyEngine.html) operation to poll the `status` field to track completion.

## Request Syntax
<a name="API_CreatePolicyEngine_RequestSyntax"></a>

```
POST /policy-engines HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "encryptionKeyArn": "{{string}}",
   "name": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreatePolicyEngine_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePolicyEngine_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreatePolicyEngine_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request with the same client token, the service returns the same response without creating a duplicate policy engine.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreatePolicyEngine_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-request-description"></a>
A human-readable description of the policy engine's purpose and scope (1-4,096 characters). This helps administrators understand the policy engine's role in the overall governance strategy. Document which Gateway this engine will be associated with, what types of tools or workflows it governs, and the team or service responsible for maintaining it. Clear descriptions are essential when managing multiple policy engines across different services or environments.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [encryptionKeyArn](#API_CreatePolicyEngine_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-request-encryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the policy engine data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [name](#API_CreatePolicyEngine_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-request-name"></a>
The customer-assigned immutable name for the policy engine. This name identifies the policy engine and cannot be changed after creation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** [tags](#API_CreatePolicyEngine_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-request-tags"></a>
A map of tag keys and values to assign to an AgentCore Policy. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreatePolicyEngine_ResponseSyntax"></a>

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
<a name="API_CreatePolicyEngine_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreatePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-response-createdAt"></a>
The timestamp when the policy engine was created. This is automatically set by the service and used for auditing and lifecycle management.  
Type: Timestamp

 ** [description](#API_CreatePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-response-description"></a>
A human-readable description of the policy engine's purpose.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [encryptionKeyArn](#API_CreatePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-response-encryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the policy engine data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [name](#API_CreatePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-response-name"></a>
The customer-assigned name of the created policy engine. This matches the name provided in the request and serves as the human-readable identifier.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*` 

 ** [policyEngineArn](#API_CreatePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-response-policyEngineArn"></a>
The Amazon Resource Name (ARN) of the created policy engine. This globally unique identifier can be used for cross-service references and IAM policy statements.  
Type: String  
Length Constraints: Minimum length of 76. Maximum length of 136.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}` 

 ** [policyEngineId](#API_CreatePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-response-policyEngineId"></a>
The unique identifier for the created policy engine. This system-generated identifier consists of the user name plus a 10-character generated suffix and is used for all subsequent policy engine operations.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [status](#API_CreatePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-response-status"></a>
The current status of the policy engine. A status of `ACTIVE` indicates the policy engine is ready for use.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [statusReasons](#API_CreatePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-response-statusReasons"></a>
Additional information about the policy engine status. This provides details about any failures or the current state of the policy engine creation process.  
Type: Array of strings

 ** [updatedAt](#API_CreatePolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicyEngine-response-updatedAt"></a>
The timestamp when the policy engine was last updated. For newly created policy engines, this matches the `createdAt` timestamp.  
Type: Timestamp

## Errors
<a name="API_CreatePolicyEngine_Errors"></a>

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
<a name="API_CreatePolicyEngine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreatePolicyEngine) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreatePolicyEngine) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreatePolicyEngine) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreatePolicyEngine) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreatePolicyEngine) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreatePolicyEngine) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreatePolicyEngine) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreatePolicyEngine) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreatePolicyEngine) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreatePolicyEngine) 