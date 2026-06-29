

# CreatePolicy
<a name="API_CreatePolicy"></a>

Creates a policy within the AgentCore Policy system. Policies provide real-time, deterministic control over agentic interactions with AgentCore Gateway. Using the Cedar policy language, you can define fine-grained policies that specify which interactions with Gateway tools are permitted based on input parameters and OAuth claims, ensuring agents operate within defined boundaries and business rules. The policy is validated during creation against the Cedar schema generated from the Gateway's tools' input schemas, which defines the available tools, their parameters, and expected data types. This is an asynchronous operation. Use the [GetPolicy](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicy.html) operation to poll the `status` field to track completion.

## Request Syntax
<a name="API_CreatePolicy_RequestSyntax"></a>

```
POST /policy-engines/{{policyEngineId}}/policies HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "definition": { ... },
   "description": "{{string}}",
   "enforcementMode": "{{string}}",
   "name": "{{string}}",
   "validationMode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreatePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyEngineId](#API_CreatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-request-uri-policyEngineId"></a>
The identifier of the policy engine which contains this policy. Policy engines group related policies and provide the execution context for policy evaluation.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

## Request Body
<a name="API_CreatePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-request-clientToken"></a>
A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don't need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without creating a duplicate policy.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [definition](#API_CreatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-request-definition"></a>
The Cedar policy statement that defines the access control rules. This contains the actual policy logic written in Cedar policy language, specifying effect (permit or forbid), principals, actions, resources, and conditions for agent behavior control.  
Type: [PolicyDefinition](API_PolicyDefinition.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [description](#API_CreatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-request-description"></a>
A human-readable description of the policy's purpose and functionality (1-4,096 characters). This helps policy administrators understand the policy's intent, business rules, and operational scope. Use this field to document why the policy exists, what business requirement it addresses, and any special considerations for maintenance. Clear descriptions are essential for policy governance, auditing, and troubleshooting.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [enforcementMode](#API_CreatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-request-enforcementMode"></a>
The enforcement mode for the policy. Run this policy in `LOG_ONLY` mode to collect data on how it affects your application. Once you are satisfied with the data gathered, switch the policy to `ACTIVE`. Defaults to `ACTIVE`.  
Type: String  
Valid Values: `ACTIVE | LOG_ONLY`   
Required: No

 ** [name](#API_CreatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-request-name"></a>
The customer-assigned immutable name for the policy. Must be unique within the account. This name is used for policy identification and cannot be changed after creation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** [validationMode](#API_CreatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-request-validationMode"></a>
The validation mode for the policy creation. Determines how Cedar analyzer validation results are handled during policy creation. FAIL\_ON\_ANY\_FINDINGS (default) runs the Cedar analyzer to validate the policy against the Cedar schema and tool context, failing creation if the analyzer detects any validation issues to ensure strict conformance. IGNORE\_ALL\_FINDINGS runs the Cedar analyzer but allows policy creation even if validation issues are detected, useful for testing or when the policy schema is evolving. Use FAIL\_ON\_ANY\_FINDINGS for production policies to ensure correctness, and IGNORE\_ALL\_FINDINGS only when you understand and accept the analyzer findings.  
Type: String  
Valid Values: `FAIL_ON_ANY_FINDINGS | IGNORE_ALL_FINDINGS`   
Required: No

## Response Syntax
<a name="API_CreatePolicy_ResponseSyntax"></a>

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
<a name="API_CreatePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-response-createdAt"></a>
The timestamp when the policy was created. This is automatically set by the service and used for auditing and lifecycle management.  
Type: Timestamp

 ** [definition](#API_CreatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-response-definition"></a>
The Cedar policy statement that was created. This is the validated policy definition that will be used for agent behavior control and access decisions.  
Type: [PolicyDefinition](API_PolicyDefinition.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [description](#API_CreatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-response-description"></a>
The human-readable description of the policy's purpose and functionality. This helps administrators understand and manage the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [enforcementMode](#API_CreatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-response-enforcementMode"></a>
The enforcement mode of the created policy.  
Type: String  
Valid Values: `ACTIVE | LOG_ONLY` 

 ** [name](#API_CreatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-response-name"></a>
The customer-assigned name of the created policy. This matches the name provided in the request and serves as the human-readable identifier for the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*` 

 ** [policyArn](#API_CreatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-response-policyArn"></a>
The Amazon Resource Name (ARN) of the created policy. This globally unique identifier can be used for cross-service references and IAM policy statements.  
Type: String  
Length Constraints: Minimum length of 96. Maximum length of 203.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}` 

 ** [policyEngineId](#API_CreatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-response-policyEngineId"></a>
The identifier of the policy engine that manages this policy. This confirms the policy engine assignment and is used for policy evaluation routing.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [policyId](#API_CreatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-response-policyId"></a>
The unique identifier for the created policy. This is a system-generated identifier consisting of the user name plus a 10-character generated suffix, used for all subsequent policy operations.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [status](#API_CreatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-response-status"></a>
The current status of the policy. A status of `ACTIVE` indicates the policy is ready for use.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [statusReasons](#API_CreatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-response-statusReasons"></a>
Additional information about the policy status. This provides details about any failures or the current state of the policy creation process.  
Type: Array of strings

 ** [updatedAt](#API_CreatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreatePolicy-response-updatedAt"></a>
The timestamp when the policy was last updated. For newly created policies, this matches the createdAt timestamp.  
Type: Timestamp

## Errors
<a name="API_CreatePolicy_Errors"></a>

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
<a name="API_CreatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreatePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreatePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreatePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreatePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreatePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreatePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreatePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreatePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreatePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreatePolicy) 