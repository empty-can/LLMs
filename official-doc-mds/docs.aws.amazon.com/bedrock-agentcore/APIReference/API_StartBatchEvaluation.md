

# StartBatchEvaluation
<a name="API_StartBatchEvaluation"></a>

Starts a batch evaluation job that evaluates agent performance across multiple sessions. Batch evaluations pull agent traces from CloudWatch Logs or an existing online evaluation configuration and run specified evaluators and insights against them.

## Request Syntax
<a name="API_StartBatchEvaluation_RequestSyntax"></a>

```
POST /evaluations/batch-evaluate HTTP/1.1
Content-type: application/json

{
   "batchEvaluationName": "{{string}}",
   "clientToken": "{{string}}",
   "dataSourceConfig": { ... },
   "description": "{{string}}",
   "evaluationMetadata": { ... },
   "evaluators": [ 
      { 
         "evaluatorId": "{{string}}"
      }
   ],
   "insights": [ 
      { 
         "insightId": "{{string}}"
      }
   ],
   "kmsKeyArn": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_StartBatchEvaluation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartBatchEvaluation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [batchEvaluationName](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-batchEvaluationName"></a>
The name of the batch evaluation. Must be unique within your account.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [clientToken](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [dataSourceConfig](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-dataSourceConfig"></a>
The data source configuration that specifies where to pull agent session traces from for evaluation.  
Type: [DataSourceConfig](API_DataSourceConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [description](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-description"></a>
The description of the batch evaluation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.  
Required: No

 ** [evaluationMetadata](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-evaluationMetadata"></a>
Optional metadata for the evaluation, including session-specific ground truth data and test scenario identifiers.  
Type: [EvaluationMetadata](API_EvaluationMetadata.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [evaluators](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-evaluators"></a>
The list of evaluators to apply during the batch evaluation. Can include both built-in evaluators and custom evaluators. Maximum of 10 evaluators.  
Type: Array of [Evaluator](API_Evaluator.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [insights](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-insights"></a>
The list of insight analyses to run against sessions during the batch evaluation. Maximum of 10 insights.  
Type: Array of [Insight](API_Insight.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [kmsKeyArn](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt evaluation data. If provided, customer data is encrypted at rest with the specified key.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [tags](#API_StartBatchEvaluation_RequestSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-request-tags"></a>
A map of tag keys and values to associate with the batch evaluation.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_StartBatchEvaluation_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "batchEvaluationArn": "string",
   "batchEvaluationId": "string",
   "batchEvaluationName": "string",
   "createdAt": "string",
   "description": "string",
   "evaluators": [ 
      { 
         "evaluatorId": "string"
      }
   ],
   "insights": [ 
      { 
         "insightId": "string"
      }
   ],
   "kmsKeyArn": "string",
   "outputConfig": { ... },
   "status": "string",
   "tags": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_StartBatchEvaluation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [batchEvaluationArn](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-batchEvaluationArn"></a>
The Amazon Resource Name (ARN) of the created batch evaluation.  
Type: String

 ** [batchEvaluationId](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-batchEvaluationId"></a>
The unique identifier of the created batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [batchEvaluationName](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-batchEvaluationName"></a>
The name of the batch evaluation.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [createdAt](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-createdAt"></a>
The timestamp when the batch evaluation was created.  
Type: Timestamp

 ** [description](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-description"></a>
The description of the batch evaluation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 200.

 ** [evaluators](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-evaluators"></a>
The list of evaluators applied during the batch evaluation.  
Type: Array of [Evaluator](API_Evaluator.md) objects

 ** [insights](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-insights"></a>
The list of insight analyses applied during the batch evaluation.  
Type: Array of [Insight](API_Insight.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [kmsKeyArn](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-kmsKeyArn"></a>
The ARN of the AWS KMS key used to encrypt evaluation data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [outputConfig](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-outputConfig"></a>
The output configuration specifying where evaluation results are written.  
Type: [OutputConfig](API_OutputConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-status"></a>
The status of the batch evaluation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | FAILED | STOPPING | STOPPED | DELETING` 

 ** [tags](#API_StartBatchEvaluation_ResponseSyntax) **   <a name="BedrockAgentCore-StartBatchEvaluation-response-tags"></a>
The tags associated with the batch evaluation.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*` 

## Errors
<a name="API_StartBatchEvaluation_Errors"></a>

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

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_StartBatchEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StartBatchEvaluation) 