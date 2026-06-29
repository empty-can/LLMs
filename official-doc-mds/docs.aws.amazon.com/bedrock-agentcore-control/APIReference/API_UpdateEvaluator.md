

# UpdateEvaluator
<a name="API_UpdateEvaluator"></a>

 Updates a custom evaluator's configuration, description, or evaluation level. Built-in evaluators cannot be updated. The evaluator must not be locked for modification. 

## Request Syntax
<a name="API_UpdateEvaluator_RequestSyntax"></a>

```
PUT /evaluators/{{evaluatorId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "evaluatorConfig": { ... },
   "kmsKeyArn": "{{string}}",
   "level": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateEvaluator_RequestParameters"></a>

The request uses the following URI parameters.

 ** [evaluatorId](#API_UpdateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateEvaluator-request-uri-evaluatorId"></a>
 The unique identifier of the evaluator to update.   
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: Yes

## Request Body
<a name="API_UpdateEvaluator_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateEvaluator-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_UpdateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateEvaluator-request-description"></a>
 The updated description of the evaluator.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [evaluatorConfig](#API_UpdateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateEvaluator-request-evaluatorConfig"></a>
 The updated configuration for the evaluator. Specify either LLM-as-a-Judge settings with instructions, rating scale, and model configuration, or code-based settings with a customer-managed Lambda function.   
Type: [EvaluatorConfig](API_EvaluatorConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [kmsKeyArn](#API_UpdateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateEvaluator-request-kmsKeyArn"></a>
 The Amazon Resource Name (ARN) of a customer managed AWS KMS key to use for encrypting sensitive evaluator data. Specify a new key ARN to rotate the encryption key, or specify a key ARN to add encryption to an evaluator that was previously created without one. When you rotate to a new key, the service decrypts the existing data with the old key and re-encrypts it with the new key. Only symmetric encryption KMS keys are supported. For more information, see [Encryption at rest for AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [level](#API_UpdateEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateEvaluator-request-level"></a>
 The updated evaluation level (`TOOL_CALL`, `TRACE`, or `SESSION`) that determines the scope of evaluation.   
Type: String  
Valid Values: `TOOL_CALL | TRACE | SESSION`   
Required: No

## Response Syntax
<a name="API_UpdateEvaluator_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "evaluatorArn": "string",
   "evaluatorId": "string",
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_UpdateEvaluator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [evaluatorArn](#API_UpdateEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateEvaluator-response-evaluatorArn"></a>
 The Amazon Resource Name (ARN) of the updated evaluator.   
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:evaluator\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$|^arn:aws[a-zA-Z-]*:bedrock-agentcore:::evaluator/Builtin.[a-zA-Z0-9_-]+` 

 ** [evaluatorId](#API_UpdateEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateEvaluator-response-evaluatorId"></a>
 The unique identifier of the updated evaluator.   
Type: String  
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})` 

 ** [status](#API_UpdateEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateEvaluator-response-status"></a>
 The status of the evaluator update operation.   
Type: String  
Valid Values: `ACTIVE | CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING` 

 ** [updatedAt](#API_UpdateEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateEvaluator-response-updatedAt"></a>
 The timestamp when the evaluator was last updated.   
Type: Timestamp

## Errors
<a name="API_UpdateEvaluator_Errors"></a>

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
<a name="API_UpdateEvaluator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateEvaluator) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateEvaluator) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateEvaluator) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateEvaluator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateEvaluator) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateEvaluator) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateEvaluator) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateEvaluator) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateEvaluator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateEvaluator) 