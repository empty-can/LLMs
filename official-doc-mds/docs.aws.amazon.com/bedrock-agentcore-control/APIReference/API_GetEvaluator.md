

# GetEvaluator
<a name="API_GetEvaluator"></a>

 Retrieves detailed information about an evaluator, including its configuration, status, and metadata. Works with both built-in and custom evaluators. 

## Request Syntax
<a name="API_GetEvaluator_RequestSyntax"></a>

```
GET /evaluators/{{evaluatorId}}?includedData={{includedData}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEvaluator_RequestParameters"></a>

The request uses the following URI parameters.

 ** [evaluatorId](#API_GetEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-request-uri-evaluatorId"></a>
 The unique identifier of the evaluator to retrieve. Can be a built-in evaluator ID (e.g., Builtin.Helpfulness) or a custom evaluator ID.   
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: Yes

 ** [includedData](#API_GetEvaluator_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-request-uri-includedData"></a>
 Controls which data is returned in the response. `ALL_DATA` (default) returns the full evaluator including decrypted instructions and rating scale. For evaluators encrypted with a customer managed AWS KMS key, this requires `kms:Decrypt` permission on the key. `METADATA_ONLY` returns evaluator metadata and model configuration without instructions or rating scale, and does not require any AWS KMS permissions.   
Valid Values: `ALL_DATA | METADATA_ONLY` 

## Request Body
<a name="API_GetEvaluator_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEvaluator_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "description": "string",
   "evaluatorArn": "string",
   "evaluatorConfig": { ... },
   "evaluatorId": "string",
   "evaluatorName": "string",
   "kmsKeyArn": "string",
   "level": "string",
   "lockedForModification": boolean,
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetEvaluator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-response-createdAt"></a>
 The timestamp when the evaluator was created.   
Type: Timestamp

 ** [description](#API_GetEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-response-description"></a>
 The description of the evaluator.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [evaluatorArn](#API_GetEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-response-evaluatorArn"></a>
 The Amazon Resource Name (ARN) of the evaluator.   
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:evaluator\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$|^arn:aws[a-zA-Z-]*:bedrock-agentcore:::evaluator/Builtin.[a-zA-Z0-9_-]+` 

 ** [evaluatorConfig](#API_GetEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-response-evaluatorConfig"></a>
 The configuration of the evaluator, including LLM-as-a-Judge or code-based settings.   
Type: [EvaluatorConfig](API_EvaluatorConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [evaluatorId](#API_GetEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-response-evaluatorId"></a>
 The unique identifier of the evaluator.   
Type: String  
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})` 

 ** [evaluatorName](#API_GetEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-response-evaluatorName"></a>
 The name of the evaluator.   
Type: String  
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9_]{0,47})` 

 ** [kmsKeyArn](#API_GetEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-response-kmsKeyArn"></a>
 The Amazon Resource Name (ARN) of the customer managed AWS KMS key used to encrypt the evaluator's sensitive data. This field is only present for evaluators encrypted with a customer managed key.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [level](#API_GetEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-response-level"></a>
 The evaluation level (`TOOL_CALL`, `TRACE`, or `SESSION`) that determines the scope of evaluation.   
Type: String  
Valid Values: `TOOL_CALL | TRACE | SESSION` 

 ** [lockedForModification](#API_GetEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-response-lockedForModification"></a>
 Whether the evaluator is locked for modification due to being referenced by active online evaluation configurations.   
Type: Boolean

 ** [status](#API_GetEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-response-status"></a>
 The current status of the evaluator.   
Type: String  
Valid Values: `ACTIVE | CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING` 

 ** [updatedAt](#API_GetEvaluator_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetEvaluator-response-updatedAt"></a>
 The timestamp when the evaluator was last updated.   
Type: Timestamp

## Errors
<a name="API_GetEvaluator_Errors"></a>

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
<a name="API_GetEvaluator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetEvaluator) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetEvaluator) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetEvaluator) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetEvaluator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetEvaluator) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetEvaluator) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetEvaluator) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetEvaluator) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetEvaluator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetEvaluator) 