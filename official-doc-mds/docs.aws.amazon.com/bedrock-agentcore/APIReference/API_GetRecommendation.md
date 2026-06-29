

# GetRecommendation
<a name="API_GetRecommendation"></a>

Retrieves detailed information about a recommendation, including its configuration, status, and results.

## Request Syntax
<a name="API_GetRecommendation_RequestSyntax"></a>

```
GET /recommendations/{{recommendationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRecommendation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recommendationId](#API_GetRecommendation_RequestSyntax) **   <a name="BedrockAgentCore-GetRecommendation-request-uri-recommendationId"></a>
The unique identifier of the recommendation to retrieve.  
Pattern: `[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}`   
Required: Yes

## Request Body
<a name="API_GetRecommendation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRecommendation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "description": "string",
   "kmsKeyArn": "string",
   "name": "string",
   "recommendationArn": "string",
   "recommendationConfig": { ... },
   "recommendationId": "string",
   "recommendationResult": { ... },
   "status": "string",
   "type": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_GetRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-createdAt"></a>
The timestamp when the recommendation was created.  
Type: Timestamp

 ** [description](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-description"></a>
The description of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [kmsKeyArn](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt recommendation data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [name](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-name"></a>
The name of the recommendation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 100.  
Pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}` 

 ** [recommendationArn](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-recommendationArn"></a>
The Amazon Resource Name (ARN) of the recommendation.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:recommendation/[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}` 

 ** [recommendationConfig](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-recommendationConfig"></a>
The configuration for the recommendation.  
Type: [RecommendationConfig](API_RecommendationConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [recommendationId](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-recommendationId"></a>
The unique identifier of the recommendation.  
Type: String  
Pattern: `[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}` 

 ** [recommendationResult](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-recommendationResult"></a>
The result of the recommendation, containing the optimized system prompt or tool descriptions. Only present when the recommendation status is `COMPLETED`.  
Type: [RecommendationResult](API_RecommendationResult.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-status"></a>
The current status of the recommendation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | DELETING` 

 ** [type](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-type"></a>
The type of recommendation.  
Type: String  
Valid Values: `SYSTEM_PROMPT_RECOMMENDATION | TOOL_DESCRIPTION_RECOMMENDATION` 

 ** [updatedAt](#API_GetRecommendation_ResponseSyntax) **   <a name="BedrockAgentCore-GetRecommendation-response-updatedAt"></a>
The timestamp when the recommendation was last updated.  
Type: Timestamp

## Errors
<a name="API_GetRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_GetRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetRecommendation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetRecommendation) 