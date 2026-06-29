

# Evaluate
<a name="API_Evaluate"></a>

 Performs on-demand evaluation of agent traces using a specified evaluator. This synchronous API accepts traces in OpenTelemetry format and returns immediate scoring results with detailed explanations.

## Request Syntax
<a name="API_Evaluate_RequestSyntax"></a>

```
POST /evaluations/evaluate/{{evaluatorId}} HTTP/1.1
Content-type: application/json

{
   "evaluationInput": { ... },
   "evaluationReferenceInputs": [ 
      { 
         "assertions": [ 
            { ... }
         ],
         "context": { ... },
         "expectedResponse": { ... },
         "expectedTrajectory": { 
            "toolNames": [ "{{string}}" ]
         }
      }
   ],
   "evaluationTarget": { ... }
}
```

## URI Request Parameters
<a name="API_Evaluate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [evaluatorId](#API_Evaluate_RequestSyntax) **   <a name="BedrockAgentCore-Evaluate-request-uri-evaluatorId"></a>
 The unique identifier of the evaluator to use for scoring. Can be a built-in evaluator (e.g., `Builtin.Helpfulness`, `Builtin.Correctness`) or a custom evaluator Id created through the control plane API.   
Pattern: `(Builtin.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: Yes

## Request Body
<a name="API_Evaluate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [evaluationInput](#API_Evaluate_RequestSyntax) **   <a name="BedrockAgentCore-Evaluate-request-evaluationInput"></a>
 The input data containing agent session spans to be evaluated. Includes a list of spans in OpenTelemetry format from supported frameworks like Strands (AgentCore Runtime) or LangGraph with OpenInference instrumentation.   
Type: [EvaluationInput](API_EvaluationInput.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [evaluationReferenceInputs](#API_Evaluate_RequestSyntax) **   <a name="BedrockAgentCore-Evaluate-request-evaluationReferenceInputs"></a>
 Ground truth data to compare against agent responses during evaluation. Allows to provide expected responses, assertions, and expected tool trajectories at different evaluation levels. Session-level reference inputs apply to the entire conversation, while trace-level reference inputs target specific request-response interactions identified by trace ID.   
Type: Array of [EvaluationReferenceInput](API_EvaluationReferenceInput.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Required: No

 ** [evaluationTarget](#API_Evaluate_RequestSyntax) **   <a name="BedrockAgentCore-Evaluate-request-evaluationTarget"></a>
 The specific trace or span IDs to evaluate within the provided input. Allows targeting evaluation at different levels: individual tool calls, single request-response interactions (traces), or entire conversation sessions.   
Type: [EvaluationTarget](API_EvaluationTarget.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## Response Syntax
<a name="API_Evaluate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "evaluationResults": [ 
      { 
         "context": { ... },
         "errorCode": "string",
         "errorMessage": "string",
         "evaluatorArn": "string",
         "evaluatorId": "string",
         "evaluatorName": "string",
         "explanation": "string",
         "ignoredReferenceInputFields": [ "string" ],
         "label": "string",
         "tokenUsage": { 
            "inputTokens": number,
            "outputTokens": number,
            "totalTokens": number
         },
         "value": number
      }
   ]
}
```

## Response Elements
<a name="API_Evaluate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [evaluationResults](#API_Evaluate_ResponseSyntax) **   <a name="BedrockAgentCore-Evaluate-response-evaluationResults"></a>
 The detailed evaluation results containing scores, explanations, and metadata. Includes the evaluator information, numerical or categorical ratings based on the evaluator's rating scale, and token usage statistics for the evaluation process.   
Type: Array of [EvaluationResultContent](API_EvaluationResultContent.md) objects

## Errors
<a name="API_Evaluate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ConflictException **   
The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.  
HTTP Status Code: 409

 ** DuplicateIdException **   
 An exception thrown when attempting to create a resource with an identifier that already exists.  
HTTP Status Code: 409

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

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
<a name="API_Evaluate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/Evaluate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Evaluate) 