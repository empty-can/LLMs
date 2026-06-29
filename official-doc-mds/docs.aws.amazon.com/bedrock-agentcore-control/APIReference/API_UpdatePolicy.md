

# UpdatePolicy
<a name="API_UpdatePolicy"></a>

Updates an existing policy within the AgentCore Policy system. This operation allows modification of the policy description and definition while maintaining the policy's identity. The updated policy is validated against the Cedar schema before being applied. This is an asynchronous operation. Use the `GetPolicy` operation to poll the `status` field to track completion.

## Request Syntax
<a name="API_UpdatePolicy_RequestSyntax"></a>

```
PATCH /policy-engines/{{policyEngineId}}/policies/{{policyId}} HTTP/1.1
Content-type: application/json

{
   "definition": { ... },
   "description": { 
      "optionalValue": "{{string}}"
   },
   "enforcementMode": "{{string}}",
   "validationMode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyEngineId](#API_UpdatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-request-uri-policyEngineId"></a>
The identifier of the policy engine that manages the policy to be updated. This ensures the policy is updated within the correct policy engine context.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** [policyId](#API_UpdatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-request-uri-policyId"></a>
The unique identifier of the policy to be updated. This must be a valid policy ID that exists within the specified policy engine.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

## Request Body
<a name="API_UpdatePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [definition](#API_UpdatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-request-definition"></a>
The new Cedar policy statement that defines the access control rules. This replaces the existing policy definition with new logic while maintaining the policy's identity.  
Type: [PolicyDefinition](API_PolicyDefinition.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [description](#API_UpdatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-request-description"></a>
The new human-readable description for the policy. This optional field allows updating the policy's documentation while keeping the same policy logic.  
Type: [UpdatedDescription](API_UpdatedDescription.md) object  
Required: No

 ** [enforcementMode](#API_UpdatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-request-enforcementMode"></a>
The enforcement mode for the policy. Run this policy in `LOG_ONLY` mode to collect data on how it affects your application. Once you are satisfied with the data gathered, switch the policy to `ACTIVE`. If you omit this field, the policy's existing enforcement mode is unchanged.  
Type: String  
Valid Values: `ACTIVE | LOG_ONLY`   
Required: No

 ** [validationMode](#API_UpdatePolicy_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-request-validationMode"></a>
The validation mode for the policy update. Determines how Cedar analyzer validation results are handled during policy updates. FAIL\_ON\_ANY\_FINDINGS runs the Cedar analyzer and fails the update if validation issues are detected, ensuring the policy conforms to the Cedar schema and tool context. IGNORE\_ALL\_FINDINGS runs the Cedar analyzer but allows updates despite validation warnings. Use FAIL\_ON\_ANY\_FINDINGS to ensure policy correctness during updates, especially when modifying policy logic or conditions.  
Type: String  
Valid Values: `FAIL_ON_ANY_FINDINGS | IGNORE_ALL_FINDINGS`   
Required: No

## Response Syntax
<a name="API_UpdatePolicy_ResponseSyntax"></a>

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
<a name="API_UpdatePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-response-createdAt"></a>
The original creation timestamp of the policy.  
Type: Timestamp

 ** [definition](#API_UpdatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-response-definition"></a>
The updated Cedar policy statement.  
Type: [PolicyDefinition](API_PolicyDefinition.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [description](#API_UpdatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-response-description"></a>
The updated description of the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [enforcementMode](#API_UpdatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-response-enforcementMode"></a>
The current enforcement mode of the updated policy.  
Type: String  
Valid Values: `ACTIVE | LOG_ONLY` 

 ** [name](#API_UpdatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-response-name"></a>
The name of the updated policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*` 

 ** [policyArn](#API_UpdatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-response-policyArn"></a>
The ARN of the updated policy.  
Type: String  
Length Constraints: Minimum length of 96. Maximum length of 203.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}` 

 ** [policyEngineId](#API_UpdatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-response-policyEngineId"></a>
The identifier of the policy engine managing the updated policy.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [policyId](#API_UpdatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-response-policyId"></a>
The unique identifier of the updated policy.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [status](#API_UpdatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-response-status"></a>
The current status of the updated policy.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [statusReasons](#API_UpdatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-response-statusReasons"></a>
Additional information about the update status.  
Type: Array of strings

 ** [updatedAt](#API_UpdatePolicy_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdatePolicy-response-updatedAt"></a>
The timestamp when the policy was last updated.  
Type: Timestamp

## Errors
<a name="API_UpdatePolicy_Errors"></a>

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
<a name="API_UpdatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdatePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdatePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdatePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdatePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdatePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdatePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdatePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdatePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdatePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdatePolicy) 