

# GetPolicyEngine
<a name="API_GetPolicyEngine"></a>

Retrieves detailed information about a specific policy engine within the AgentCore Policy system. This operation returns the complete policy engine configuration, metadata, and current status, allowing administrators to review and manage policy engine settings.

## Request Syntax
<a name="API_GetPolicyEngine_RequestSyntax"></a>

```
GET /policy-engines/{{policyEngineId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPolicyEngine_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyEngineId](#API_GetPolicyEngine_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyEngine-request-uri-policyEngineId"></a>
The unique identifier of the policy engine to be retrieved. This must be a valid policy engine ID that exists within the account.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

## Request Body
<a name="API_GetPolicyEngine_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPolicyEngine_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetPolicyEngine_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetPolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyEngine-response-createdAt"></a>
The timestamp when the policy engine was originally created.  
Type: Timestamp

 ** [description](#API_GetPolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyEngine-response-description"></a>
The human-readable description of the policy engine's purpose and scope. This helps administrators understand the policy engine's role in governance.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [encryptionKeyArn](#API_GetPolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyEngine-response-encryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the policy engine data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [name](#API_GetPolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyEngine-response-name"></a>
The customer-assigned name of the policy engine. This is the human-readable identifier that was specified when the policy engine was created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*` 

 ** [policyEngineArn](#API_GetPolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyEngine-response-policyEngineArn"></a>
The Amazon Resource Name (ARN) of the policy engine. This globally unique identifier can be used for cross-service references and IAM policy statements.  
Type: String  
Length Constraints: Minimum length of 76. Maximum length of 136.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}` 

 ** [policyEngineId](#API_GetPolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyEngine-response-policyEngineId"></a>
The unique identifier of the retrieved policy engine. This matches the policy engine ID provided in the request and serves as the system identifier.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [status](#API_GetPolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyEngine-response-status"></a>
The current status of the policy engine.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [statusReasons](#API_GetPolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyEngine-response-statusReasons"></a>
Additional information about the policy engine status. This provides details about any failures or the current state of the policy engine.  
Type: Array of strings

 ** [updatedAt](#API_GetPolicyEngine_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyEngine-response-updatedAt"></a>
The timestamp when the policy engine was last modified. This tracks the most recent changes to the policy engine configuration.  
Type: Timestamp

## Errors
<a name="API_GetPolicyEngine_Errors"></a>

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
<a name="API_GetPolicyEngine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetPolicyEngine) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetPolicyEngine) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetPolicyEngine) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetPolicyEngine) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetPolicyEngine) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetPolicyEngine) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetPolicyEngine) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetPolicyEngine) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetPolicyEngine) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetPolicyEngine) 