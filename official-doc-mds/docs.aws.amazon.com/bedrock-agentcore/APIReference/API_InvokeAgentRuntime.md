

# InvokeAgentRuntime
<a name="API_InvokeAgentRuntime"></a>

Sends a request to an agent or tool hosted in an Amazon Bedrock AgentCore Runtime and receives responses in real-time. 

To invoke an agent, you can specify either the AgentCore Runtime ARN or the agent ID with an account ID, and provide a payload containing your request. When you use the agent ID instead of the full ARN, you don't need to URL-encode the identifier. You can optionally specify a qualifier to target a specific endpoint of the agent.

This operation supports streaming responses, allowing you to receive partial responses as they become available. We recommend using pagination to ensure that the operation returns quickly and successfully when processing large responses.

For example code, see [Invoke an AgentCore Runtime agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html). 

If you're integrating your agent with OAuth, you can't use the AWS SDK to call `InvokeAgentRuntime`. Instead, make a HTTPS request to `InvokeAgentRuntime`. For an example, see [Authenticate and authorize with Inbound Auth and Outbound Auth](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html).

To use this operation, you must have the `bedrock-agentcore:InvokeAgentRuntime` permission. If you are making a call to `InvokeAgentRuntime` on behalf of a user ID with the `X-Amzn-Bedrock-AgentCore-Runtime-User-Id` header, You require permissions to both actions (`bedrock-agentcore:InvokeAgentRuntime` and `bedrock-agentcore:InvokeAgentRuntimeForUser`). 

## Request Syntax
<a name="API_InvokeAgentRuntime_RequestSyntax"></a>

```
POST /runtimes/{{agentRuntimeArn}}/invocations?accountId={{accountId}}&qualifier={{qualifier}} HTTP/1.1
Content-Type: {{contentType}}
Accept: {{accept}}
Mcp-Session-Id: {{mcpSessionId}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
Mcp-Protocol-Version: {{mcpProtocolVersion}}
X-Amzn-Bedrock-AgentCore-Runtime-User-Id: {{runtimeUserId}}
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
tracestate: {{traceState}}
baggage: {{baggage}}

{{payload}}
```

## URI Request Parameters
<a name="API_InvokeAgentRuntime_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accept](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-accept"></a>
The desired MIME type for the response from the agent runtime. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [accountId](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-uri-accountId"></a>
The identifier of the AWS account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for `agentRuntimeArn`.  
Pattern: `[0-9]{12}` 

 ** [agentRuntimeArn](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-uri-agentRuntimeArn"></a>
The identifier of the agent runtime to invoke. You can specify either the full AWS Resource Name (ARN) or the agent ID. If you use the agent ID, you must also provide the `accountId` query parameter.  
Required: Yes

 ** [baggage](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-baggage"></a>
Additional context information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 8192.

 ** [contentType](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-contentType"></a>
The MIME type of the input data in the payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.  
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [mcpProtocolVersion](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-mcpProtocolVersion"></a>
The version of the MCP protocol being used.  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [mcpSessionId](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-mcpSessionId"></a>
The identifier of the MCP session.  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [qualifier](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-uri-qualifier"></a>
The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.

 ** [runtimeSessionId](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-runtimeSessionId"></a>
The identifier of the runtime session.  
Length Constraints: Minimum length of 33. Maximum length of 256.

 ** [runtimeUserId](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-runtimeUserId"></a>
The identifier of the runtime user.  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [traceId](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [traceParent](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [traceState](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-traceState"></a>
The trace state information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 512.

## Request Body
<a name="API_InvokeAgentRuntime_RequestBody"></a>

The request accepts the following binary data.

 ** [payload](#API_InvokeAgentRuntime_RequestSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-request-payload"></a>
The input data to send to the agent runtime. The format of this data depends on the specific agent configuration and must match the specified content type. For most agents, this is a JSON object containing the user's request.  
Length Constraints: Minimum length of 0. Maximum length of 100000000.  
Required: Yes

## Response Syntax
<a name="API_InvokeAgentRuntime_ResponseSyntax"></a>

```
HTTP/1.1 {{statusCode}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
Mcp-Session-Id: {{mcpSessionId}}
Mcp-Protocol-Version: {{mcpProtocolVersion}}
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
tracestate: {{traceState}}
baggage: {{baggage}}
Content-Type: {{contentType}}

{{response}}
```

## Response Elements
<a name="API_InvokeAgentRuntime_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [statusCode](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-statusCode"></a>
The HTTP status code of the response. A status code of 200 indicates a successful operation. Other status codes indicate various error conditions.

The response returns the following HTTP headers.

 ** [baggage](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-baggage"></a>
Additional context information for distributed tracing.

 ** [contentType](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-contentType"></a>
The MIME type of the response data. This indicates how to interpret the response data. Common values include application/json for JSON data.

 ** [mcpProtocolVersion](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-mcpProtocolVersion"></a>
The version of the MCP protocol being used.

 ** [mcpSessionId](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-mcpSessionId"></a>
The identifier of the MCP session.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

 ** [runtimeSessionId](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-runtimeSessionId"></a>
The identifier of the runtime session.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

 ** [traceId](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-traceId"></a>
The trace identifier for request tracking.

 ** [traceParent](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-traceParent"></a>
The parent trace information for distributed tracing.

 ** [traceState](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-traceState"></a>
The trace state information for distributed tracing.

The response returns the following as the HTTP body.

 ** [response](#API_InvokeAgentRuntime_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeAgentRuntime-response-response"></a>
The response data from the agent runtime. The format of this data depends on the specific agent configuration and the requested accept type. For most agents, this is a JSON object containing the agent's response to the user's request.

## Errors
<a name="API_InvokeAgentRuntime_Errors"></a>

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

 ** RetryableConflictException **   
The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 409

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
<a name="API_InvokeAgentRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntime) 