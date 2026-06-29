

# StartPolicyGeneration
<a name="API_StartPolicyGeneration"></a>

Initiates the AI-powered generation of Cedar policies from natural language descriptions within the AgentCore Policy system. This feature enables both technical and non-technical users to create policies by describing their authorization requirements in plain English, which is then automatically translated into formal Cedar policy statements. The generation process analyzes the natural language input along with the Gateway's tool context to produce validated policy options. Generated policy assets are automatically deleted after 7 days, so you should review and create policies from the generated assets within this timeframe. Once created, policies are permanent and not subject to this expiration. Generated policies should be reviewed and tested in log-only mode before deploying to production. Use this when you want to describe policy intent naturally rather than learning Cedar syntax, though generated policies may require refinement for complex scenarios.

## Request Syntax
<a name="API_StartPolicyGeneration_RequestSyntax"></a>

```
POST /policy-engines/{{policyEngineId}}/policy-generations HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "content": { ... },
   "name": "{{string}}",
   "resource": { ... }
}
```

## URI Request Parameters
<a name="API_StartPolicyGeneration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyEngineId](#API_StartPolicyGeneration_RequestSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-request-uri-policyEngineId"></a>
The identifier of the policy engine that provides the context for policy generation. This engine's schema and tool context are used to ensure generated policies are valid and applicable.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

## Request Body
<a name="API_StartPolicyGeneration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartPolicyGeneration_RequestSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-request-clientToken"></a>
A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don't need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without starting a duplicate generation.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [content](#API_StartPolicyGeneration_RequestSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-request-content"></a>
The natural language description of the desired policy behavior. This content is processed by AI to generate corresponding Cedar policy statements that match the described intent.  
Type: [Content](API_Content.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [name](#API_StartPolicyGeneration_RequestSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-request-name"></a>
A customer-assigned name for the policy generation request. This helps track and identify generation operations, especially when running multiple generations simultaneously.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** [resource](#API_StartPolicyGeneration_RequestSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-request-resource"></a>
The resource information that provides context for policy generation. This helps the AI understand the target resources and generate appropriate access control rules.  
Type: [Resource](API_Resource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_StartPolicyGeneration_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_StartPolicyGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_StartPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-response-createdAt"></a>
The timestamp when the policy generation request was created.  
Type: Timestamp

 ** [findings](#API_StartPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-response-findings"></a>
Initial findings from the policy generation process.  
Type: String

 ** [name](#API_StartPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-response-name"></a>
The customer-assigned name for the policy generation request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[A-Za-z][A-Za-z0-9_]*` 

 ** [policyEngineId](#API_StartPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-response-policyEngineId"></a>
The identifier of the policy engine associated with the started policy generation.   
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [policyGenerationArn](#API_StartPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-response-policyGenerationArn"></a>
The ARN of the created policy generation request.  
Type: String  
Length Constraints: Minimum length of 103. Maximum length of 210.  
Pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy-generation/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}` 

 ** [policyGenerationId](#API_StartPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-response-policyGenerationId"></a>
The unique identifier assigned to the policy generation request for tracking progress.   
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}` 

 ** [resource](#API_StartPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-response-resource"></a>
The resource information associated with the policy generation request.  
Type: [Resource](API_Resource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_StartPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-response-status"></a>
The initial status of the policy generation request.  
Type: String  
Valid Values: `GENERATING | GENERATED | GENERATE_FAILED | DELETE_FAILED` 

 ** [statusReasons](#API_StartPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-response-statusReasons"></a>
Additional information about the generation status.  
Type: Array of strings

 ** [updatedAt](#API_StartPolicyGeneration_ResponseSyntax) **   <a name="bedrockagentcorecontrol-StartPolicyGeneration-response-updatedAt"></a>
The timestamp when the policy generation was last updated.  
Type: Timestamp

## Errors
<a name="API_StartPolicyGeneration_Errors"></a>

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
<a name="API_StartPolicyGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/StartPolicyGeneration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/StartPolicyGeneration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/StartPolicyGeneration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/StartPolicyGeneration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/StartPolicyGeneration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/StartPolicyGeneration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/StartPolicyGeneration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/StartPolicyGeneration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/StartPolicyGeneration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/StartPolicyGeneration) 