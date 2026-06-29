

# GetPolicyGeneration
<a name="API_GetPolicyGeneration"></a>

Retrieves information about a policy generation request within the AgentCore Policy system. Policy generation converts natural language descriptions into Cedar policy statements using AI-powered translation, enabling non-technical users to create policies.

## Request Syntax
<a name="API_GetPolicyGeneration_RequestSyntax"></a>

```
GET /policy-engines/{{policyEngineId}}/policy-generations/{{policyGenerationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPolicyGeneration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyEngineId](#API_GetPolicyGeneration_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-request-uri-policyEngineId"></a>
The identifier of the policy engine associated with the policy generation request. This provides the context for the generation operation and schema validation.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** [policyGenerationId](#API_GetPolicyGeneration_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-request-uri-policyGenerationId"></a>
The unique identifier of the policy generation request to be retrieved. This must be a valid generation ID from a previous [StartPolicyGeneration](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html) call.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

## Request Body
<a name="API_GetPolicyGeneration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPolicyGeneration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "findings": "string",
   "name": "string",
   "policyEngineId": "string",
   "policyGenerationArn": "string",
   "policyGenerationId": "string",
   "resource": { ... },
   "status": "string",
   "statusReasons": [ "string" ],
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetPolicyGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-response-createdAt"></a>
The timestamp when the policy generation request was created. This is used for tracking and auditing generation operations and their lifecycle.  
Type: Timestamp

 ** [findings](#API_GetPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-response-findings"></a>
The findings and results from the policy generation process. This includes any issues, recommendations, validation results, or insights from the generated policies.  
Type: String

 ** [name](#API_GetPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-response-name"></a>
The customer-assigned name for the policy generation request. This helps identify and track generation operations across multiple requests.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*` 

 ** [policyEngineId](#API_GetPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-response-policyEngineId"></a>
The identifier of the policy engine associated with this policy generation. This confirms the policy engine context for the generation operation.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [policyGenerationArn](#API_GetPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-response-policyGenerationArn"></a>
The Amazon Resource Name (ARN) of the policy generation. This globally unique identifier can be used for tracking, auditing, and cross-service references.  
Type: String  
Length Constraints: Minimum length of 103. Maximum length of 210.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy-generation/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}` 

 ** [policyGenerationId](#API_GetPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-response-policyGenerationId"></a>
The unique identifier of the policy generation request. This matches the generation ID provided in the request and serves as the tracking identifier.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [resource](#API_GetPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-response-resource"></a>
The resource information associated with the policy generation. This provides context about the target resources for which the policies are being generated.  
Type: [Resource](API_Resource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-response-status"></a>
The current status of the policy generation. This indicates whether the generation is in progress, completed successfully, or failed during processing.  
Type: String  
Valid Values: `GENERATING | GENERATED | GENERATE_FAILED | DELETE_FAILED` 

 ** [statusReasons](#API_GetPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-response-statusReasons"></a>
Additional information about the generation status. This provides details about any failures, warnings, or the current state of the generation process.  
Type: Array of strings

 ** [updatedAt](#API_GetPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetPolicyGeneration-response-updatedAt"></a>
The timestamp when the policy generation was last updated. This tracks the progress of the generation process and any status changes.  
Type: Timestamp

## Errors
<a name="API_GetPolicyGeneration_Errors"></a>

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
<a name="API_GetPolicyGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetPolicyGeneration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetPolicyGeneration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetPolicyGeneration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetPolicyGeneration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetPolicyGeneration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetPolicyGeneration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetPolicyGeneration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetPolicyGeneration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetPolicyGeneration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetPolicyGeneration) 