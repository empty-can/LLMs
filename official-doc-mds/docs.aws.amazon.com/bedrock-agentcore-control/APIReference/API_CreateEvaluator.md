

# CreateEvaluator
<a name="API_CreateEvaluator"></a>

 Creates a custom evaluator for agent quality assessment. Custom evaluators can use either LLM-as-a-Judge configurations with user-defined prompts, rating scales, and model settings, or code-based configurations with customer-managed Lambda functions to evaluate agent performance at tool call, trace, or session levels. 

## Request Syntax
<a name="API_CreateEvaluator_RequestSyntax"></a>

```
POST /evaluators/create HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "evaluatorConfig": { ... },
   "evaluatorName": "{{string}}",
   "kmsKeyArn": "{{string}}",
   "level": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateEvaluator_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEvaluator_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateEvaluator-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateEvaluator-request-description"></a>
 The description of the evaluator that explains its purpose and evaluation criteria.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [evaluatorConfig](#API_CreateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateEvaluator-request-evaluatorConfig"></a>
 The configuration for the evaluator. Specify either LLM-as-a-Judge settings with instructions, rating scale, and model configuration, or code-based settings with a customer-managed Lambda function.   
Type: [EvaluatorConfig](API_EvaluatorConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [evaluatorName](#API_CreateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateEvaluator-request-evaluatorName"></a>
 The name of the evaluator. Must be unique within your account.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [kmsKeyArn](#API_CreateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateEvaluator-request-kmsKeyArn"></a>
 The Amazon Resource Name (ARN) of a customer managed AWS KMS key to use for encrypting sensitive evaluator data, including instructions and rating scale. If you don't specify a KMS key, the evaluator data is encrypted with an AWS owned key. Only symmetric encryption KMS keys are supported. For more information, see [Encryption at rest for AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [level](#API_CreateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateEvaluator-request-level"></a>
 The evaluation level that determines the scope of evaluation. Valid values are `TOOL_CALL` for individual tool invocations, `TRACE` for single request-response interactions, or `SESSION` for entire conversation sessions.   
Type: String  
Valid Values: `TOOL_CALL | TRACE | SESSION`   
Required: Yes

 ** [tags](#API_CreateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateEvaluator-request-tags"></a>
A map of tag keys and values to assign to an AgentCore Evaluator. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateEvaluator_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": number,
   "evaluatorArn": "string",
   "evaluatorId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateEvaluator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_CreateEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateEvaluator-response-createdAt"></a>
 The timestamp when the evaluator was created.   
Type: Timestamp

 ** [evaluatorArn](#API_CreateEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateEvaluator-response-evaluatorArn"></a>
 The Amazon Resource Name (ARN) of the created evaluator.   
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:evaluator\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}` 

 ** [evaluatorId](#API_CreateEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateEvaluator-response-evaluatorId"></a>
 The unique identifier of the created evaluator.   
Type: String  
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})` 

 ** [status](#API_CreateEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateEvaluator-response-status"></a>
 The status of the evaluator creation operation.   
Type: String  
Valid Values: `ACTIVE | CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING` 

## Errors
<a name="API_CreateEvaluator_Errors"></a>

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
<a name="API_CreateEvaluator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateEvaluator) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateEvaluator) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateEvaluator) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateEvaluator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateEvaluator) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateEvaluator) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateEvaluator) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateEvaluator) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateEvaluator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateEvaluator) 