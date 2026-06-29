

# StopRuntimeSession
<a name="API_StopRuntimeSession"></a>

Stops a session that is running in an running AgentCore Runtime agent.

## Request Syntax
<a name="API_StopRuntimeSession_RequestSyntax"></a>

```
POST /runtimes/{{agentRuntimeArn}}/stopruntimesession?qualifier={{qualifier}} HTTP/1.1
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
Content-type: application/json

{
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopRuntimeSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentRuntimeArn](#API_StopRuntimeSession_RequestSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-request-uri-agentRuntimeArn"></a>
The ARN of the agent that contains the session that you want to stop.  
Required: Yes

 ** [qualifier](#API_StopRuntimeSession_RequestSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-request-uri-qualifier"></a>
Optional qualifier to specify an agent alias, such as `prod`code> or `dev`. If you don't provide a value, the DEFAULT alias is used. 

 ** [runtimeSessionId](#API_StopRuntimeSession_RequestSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-request-runtimeSessionId"></a>
The ID of the session that you want to stop.  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Required: Yes

## Request Body
<a name="API_StopRuntimeSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StopRuntimeSession_RequestSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-request-clientToken"></a>
Idempotent token used to identify the request. If you use the same token with multiple requests, the same response is returned. Use ClientToken to prevent the same request from being processed more than once.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

## Response Syntax
<a name="API_StopRuntimeSession_ResponseSyntax"></a>

```
HTTP/1.1 {{statusCode}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
```

## Response Elements
<a name="API_StopRuntimeSession_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [statusCode](#API_StopRuntimeSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-response-statusCode"></a>
The status code of the request to stop the session.

The response returns the following HTTP headers.

 ** [runtimeSessionId](#API_StopRuntimeSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopRuntimeSession-response-runtimeSessionId"></a>
The ID of the session that you requested to stop.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

## Errors
<a name="API_StopRuntimeSession_Errors"></a>

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

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_StopRuntimeSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StopRuntimeSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StopRuntimeSession) 