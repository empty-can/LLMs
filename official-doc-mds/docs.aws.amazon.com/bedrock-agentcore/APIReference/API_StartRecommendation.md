

# StartRecommendation
<a name="API_StartRecommendation"></a>

Starts a recommendation job that analyzes agent traces and generates optimization suggestions for system prompts or tool descriptions to improve agent performance.

## Request Syntax
<a name="API_StartRecommendation_RequestSyntax"></a>

```
POST /recommendations HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "kmsKeyArn": "{{string}}",
   "name": "{{string}}",
   "recommendationConfig": { ... },
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartRecommendation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartRecommendation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-description"></a>
The description of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4096.  
Required: No

 ** [kmsKeyArn](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt recommendation data. If provided, customer data is encrypted at rest with the specified key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [name](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-name"></a>
The name of the recommendation. Must be unique within your account.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`   
Required: Yes

 ** [recommendationConfig](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-recommendationConfig"></a>
The configuration for the recommendation, including the input to optimize, agent traces to analyze, and evaluation settings.  
Type: [RecommendationConfig](API_RecommendationConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [tags](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-tags"></a>
A map of tag keys and values to associate with the recommendation.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** [type](#API_StartRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-StartRecommendation-request-type"></a>
The type of recommendation to generate. Valid values are `SYSTEM_PROMPT_RECOMMENDATION` for system prompt optimization or `TOOL_DESCRIPTION_RECOMMENDATION` for tool description optimization.  
Type: String  
Valid Values: `SYSTEM_PROMPT_RECOMMENDATION | TOOL_DESCRIPTION_RECOMMENDATION`   
Required: Yes

## Response Syntax
<a name="API_StartRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": "string",
   "description": "string",
   "name": "string",
   "recommendationArn": "string",
   "recommendationConfig": { ... },
   "recommendationId": "string",
   "status": "string",
   "type": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_StartRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-createdAt"></a>
The timestamp when the recommendation was created.  
Type: Timestamp

 ** [description](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-description"></a>
The description of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [name](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-name"></a>
The name of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}` 

 ** [recommendationArn](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-recommendationArn"></a>
The Amazon Resource Name (ARN) of the created recommendation.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:recommendation/[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}` 

 ** [recommendationConfig](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-recommendationConfig"></a>
The configuration for the recommendation.  
Type: [RecommendationConfig](API_RecommendationConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [recommendationId](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-recommendationId"></a>
The unique identifier of the created recommendation.  
Type: String  
Pattern: `[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}` 

 ** [status](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-status"></a>
The status of the recommendation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | DELETING` 

 ** [type](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-type"></a>
The type of recommendation.  
Type: String  
Valid Values: `SYSTEM_PROMPT_RECOMMENDATION | TOOL_DESCRIPTION_RECOMMENDATION` 

 ** [updatedAt](#API_StartRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-StartRecommendation-response-updatedAt"></a>
The timestamp when the recommendation was last updated.  
Type: Timestamp

## Errors
<a name="API_StartRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_StartRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StartRecommendation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StartRecommendation) 