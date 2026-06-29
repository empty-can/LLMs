

# InvokeAgentRuntimeCommand
<a name="API_InvokeAgentRuntimeCommand"></a>

Executes a command in a runtime session container and streams the output back to the caller. This operation allows you to run shell commands within the agent runtime environment and receive real-time streaming responses including standard output and standard error.

To invoke a command, you must specify the agent runtime ARN and a runtime session ID. The command execution supports streaming responses, allowing you to receive output as it becomes available through `contentStart`, `contentDelta`, and `contentStop` events.

To use this operation, you must have the `bedrock-agentcore:InvokeAgentRuntimeCommand` permission.

## Request Syntax
<a name="API_InvokeAgentRuntimeCommand_RequestSyntax"></a>

```
POST /runtimes/{{agentRuntimeArn}}/commands?accountId={{accountId}}&qualifier={{qualifier}} HTTP/1.1
Content-Type: {{contentType}}
Accept: {{accept}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
tracestate: {{traceState}}
baggage: {{baggage}}
Content-type: application/json

{
   "command": "{{string}}",
   "timeout": {{number}}
}
```

## URI Request Parameters
<a name="API_InvokeAgentRuntimeCommand_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accept](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-accept"></a>
The desired MIME type for the response from the agent runtime command. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [accountId](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-uri-accountId"></a>
The identifier of the AWS account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for `agentRuntimeArn`.  
Pattern: `[0-9]{12}` 

 ** [agentRuntimeArn](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-uri-agentRuntimeArn"></a>
The Amazon Resource Name (ARN) of the agent runtime on which to execute the command. This identifies the specific agent runtime environment where the command will run.  
Required: Yes

 ** [baggage](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-baggage"></a>
Additional context information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 8192.

 ** [contentType](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-contentType"></a>
The MIME type of the input data in the request payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [qualifier](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-uri-qualifier"></a>
The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.

 ** [runtimeSessionId](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-runtimeSessionId"></a>
The unique identifier of the runtime session in which to execute the command. This session ID is used to maintain state and context across multiple command invocations.  
Length Constraints: Minimum length of 33. Maximum length of 256.

 ** [traceId](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceState](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-traceState"></a>
The trace state information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 512.

## Request Body
<a name="API_InvokeAgentRuntimeCommand_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [command](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-command"></a>
The shell command to execute on the agent runtime. This command is executed in the runtime environment and its output is streamed back to the caller.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Required: Yes

 ** [timeout](#API_InvokeAgentRuntimeCommand_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-request-timeout"></a>
The maximum duration in seconds to wait for the command to complete. If the command execution exceeds this timeout, it will be terminated. Default is 300 seconds. Minimum is 1 second. Maximum is 3600 seconds.  
Type: Integer  
Required: No

## Response Syntax
<a name="API_InvokeAgentRuntimeCommand_ResponseSyntax"></a>

```
HTTP/1.1 {{statusCode}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
tracestate: {{traceState}}
baggage: {{baggage}}
Content-Type: {{contentType}}
Content-type: application/json

{
   "accessDeniedException": { 
   },
   "chunk": { 
      "contentDelta": { 
         "stderr": "string",
         "stdout": "string"
      },
      "contentStart": { 
      },
      "contentStop": { 
         "exitCode": number,
         "status": "string"
      }
   },
   "internalServerException": { 
   },
   "resourceNotFoundException": { 
   },
   "runtimeClientError": { 
   },
   "serviceQuotaExceededException": { 
   },
   "throttlingException": { 
   },
   "validationException": { 
   }
}
```

## Response Elements
<a name="API_InvokeAgentRuntimeCommand_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [statusCode](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-statusCode"></a>
The HTTP status code of the response. A status code of 200 indicates a successful operation. Other status codes indicate various error conditions.

The response returns the following HTTP headers.

 ** [baggage](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-baggage"></a>
Additional context information for distributed tracing.

 ** [contentType](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-contentType"></a>
The MIME type of the response data. This indicates how to interpret the response data. Common values include application/json for JSON data.

 ** [runtimeSessionId](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-runtimeSessionId"></a>
The unique identifier of the runtime session in which the command was executed.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

 ** [traceId](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-traceId"></a>
The trace identifier for request tracking.

 ** [traceParent](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-traceParent"></a>
The parent trace information for distributed tracing.

 ** [traceState](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-traceState"></a>
The trace state information for distributed tracing.

The following data is returned in JSON format by the service.

 ** [accessDeniedException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-accessDeniedException"></a>
Exception events for error streaming.  
Type: Exception  
HTTP Status Code: 403

 ** [chunk](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-chunk"></a>
A response chunk containing command execution events such as content start, content delta, or content stop events.  
Type: [ResponseChunk](API_ResponseChunk.md) object

 ** [internalServerException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 500

 ** [resourceNotFoundException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-resourceNotFoundException"></a>
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
Type: Exception  
HTTP Status Code: 404

 ** [runtimeClientError](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-runtimeClientError"></a>
The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.  
Type: Exception  
HTTP Status Code: 424

 ** [serviceQuotaExceededException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-serviceQuotaExceededException"></a>
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
Type: Exception  
HTTP Status Code: 402

 ** [throttlingException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-throttlingException"></a>
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 429

 ** [validationException](#API_InvokeAgentRuntimeCommand_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntimeCommand-response-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
Type: Exception  
HTTP Status Code: 400

## Errors
<a name="API_InvokeAgentRuntimeCommand_Errors"></a>

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

 ** RuntimeClientError **   
The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.  
HTTP Status Code: 424

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
<a name="API_InvokeAgentRuntimeCommand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommand) 