

# StartFlowExecution
<a name="API_agent-runtime_StartFlowExecution"></a>

Starts an execution of an Amazon Bedrock flow. Unlike flows that run until completion or time out after five minutes, flow executions let you run flows asynchronously for longer durations. Flow executions also yield control so that your application can perform other tasks.

This operation returns an Amazon Resource Name (ARN) that you can use to track and manage your flow execution.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Request Syntax
<a name="API_agent-runtime_StartFlowExecution_RequestSyntax"></a>

```
POST /flows/{{flowIdentifier}}/aliases/{{flowAliasIdentifier}}/executions HTTP/1.1
Content-type: application/json

{
   "flowExecutionName": "{{string}}",
   "inputs": [ 
      { 
         "content": { ... },
         "nodeInputName": "{{string}}",
         "nodeName": "{{string}}",
         "nodeOutputName": "{{string}}"
      }
   ],
   "modelPerformanceConfiguration": { 
      "performanceConfig": { 
         "latency": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_agent-runtime_StartFlowExecution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowAliasIdentifier](#API_agent-runtime_StartFlowExecution_RequestSyntax) **   <a name="bedrock-agent-runtime_StartFlowExecution-request-uri-flowAliasIdentifier"></a>
The unique identifier of the flow alias to use for the flow execution.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** [flowIdentifier](#API_agent-runtime_StartFlowExecution_RequestSyntax) **   <a name="bedrock-agent-runtime_StartFlowExecution-request-uri-flowIdentifier"></a>
The unique identifier of the flow to execute.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

## Request Body
<a name="API_agent-runtime_StartFlowExecution_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [flowExecutionName](#API_agent-runtime_StartFlowExecution_RequestSyntax) **   <a name="bedrock-agent-runtime_StartFlowExecution-request-flowExecutionName"></a>
The unique name for the flow execution. If you don't provide one, a system-generated name is used.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-zA-Z0-9-]{1,36}`   
Required: No

 ** [inputs](#API_agent-runtime_StartFlowExecution_RequestSyntax) **   <a name="bedrock-agent-runtime_StartFlowExecution-request-inputs"></a>
The input data required for the flow execution. This must match the input schema defined in the flow.  
Type: Array of [FlowInput](API_agent-runtime_FlowInput.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** [modelPerformanceConfiguration](#API_agent-runtime_StartFlowExecution_RequestSyntax) **   <a name="bedrock-agent-runtime_StartFlowExecution-request-modelPerformanceConfiguration"></a>
The performance settings for the foundation model used in the flow execution.  
Type: [ModelPerformanceConfiguration](API_agent-runtime_ModelPerformanceConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_agent-runtime_StartFlowExecution_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "executionArn": "string"
}
```

## Response Elements
<a name="API_agent-runtime_StartFlowExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionArn](#API_agent-runtime_StartFlowExecution_ResponseSyntax) **   <a name="bedrock-agent-runtime_StartFlowExecution-response-executionArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the flow execution.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9-]{1,36}$|^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10}/execution/[a-zA-Z0-9-]{1,36})` 

## Errors
<a name="API_agent-runtime_StartFlowExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** BadGatewayException **   
There was an issue with a dependency due to a server issue. Retry your request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 502

 ** ConflictException **   
There was a conflict performing an operation. Resolve the conflict and retry your request.  
HTTP Status Code: 409

 ** DependencyFailedException **   
There was an issue with a dependency. Check the resource configurations and retry the request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 424

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_agent-runtime_StartFlowExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/StartFlowExecution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/StartFlowExecution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/StartFlowExecution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/StartFlowExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/StartFlowExecution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/StartFlowExecution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/StartFlowExecution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/StartFlowExecution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/StartFlowExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/StartFlowExecution) 