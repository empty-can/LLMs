

# GetPolicySummary
<a name="API_GetPolicySummary"></a>

Retrieves a metadata-only summary of a specific policy without decrypting customer content. This lightweight read operation returns resource identifiers, status, and timestamps, but does not include the policy definition, description, or status reasons. Because this operation does not require access to the customer's AWS KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.

## Request Syntax
<a name="API_GetPolicySummary_RequestSyntax"></a>

```
GET /policy-engines/{{policyEngineId}}/policy-summaries/{{policyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPolicySummary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyEngineId](#API_GetPolicySummary_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetPolicySummary-request-uri-policyEngineId"></a>
The identifier of the policy engine that manages the policy to retrieve the summary for.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** [policyId](#API_GetPolicySummary_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetPolicySummary-request-uri-policyId"></a>
The unique identifier of the policy to retrieve the summary for. This must be a valid policy ID that exists within the specified policy engine.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

## Request Body
<a name="API_GetPolicySummary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPolicySummary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "enforcementMode": "string",
   "name": "string",
   "policyArn": "string",
   "policyEngineId": "string",
   "policyId": "string",
   "status": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetPolicySummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetPolicySummary_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicySummary-response-createdAt"></a>
The timestamp when the policy was originally created.  
Type: Timestamp

 ** [enforcementMode](#API_GetPolicySummary_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicySummary-response-enforcementMode"></a>
The current enforcement mode of the policy.  
Type: String  
Valid Values: `ACTIVE | LOG_ONLY` 

 ** [name](#API_GetPolicySummary_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicySummary-response-name"></a>
The customer-assigned name of the policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*` 

 ** [policyArn](#API_GetPolicySummary_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicySummary-response-policyArn"></a>
The Amazon Resource Name (ARN) of the policy.  
Type: String  
Length Constraints: Minimum length of 96. Maximum length of 203.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}` 

 ** [policyEngineId](#API_GetPolicySummary_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicySummary-response-policyEngineId"></a>
The identifier of the policy engine that manages this policy.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [policyId](#API_GetPolicySummary_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicySummary-response-policyId"></a>
The unique identifier of the policy.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [status](#API_GetPolicySummary_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicySummary-response-status"></a>
The current status of the policy.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED` 

 ** [updatedAt](#API_GetPolicySummary_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicySummary-response-updatedAt"></a>
The timestamp when the policy was last modified.  
Type: Timestamp

## Errors
<a name="API_GetPolicySummary_Errors"></a>

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
<a name="API_GetPolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetPolicySummary) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetPolicySummary) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetPolicySummary) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetPolicySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetPolicySummary) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetPolicySummary) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetPolicySummary) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetPolicySummary) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetPolicySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetPolicySummary) 