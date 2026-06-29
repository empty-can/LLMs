

# GetAgentCard
<a name="API_GetAgentCard"></a>

Retrieves the A2A agent card associated with an AgentCore Runtime agent.

## Request Syntax
<a name="API_GetAgentCard_RequestSyntax"></a>

```
GET /runtimes/{{agentRuntimeArn}}/invocations/.well-known/agent-card.json?qualifier={{qualifier}} HTTP/1.1
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
```

## URI Request Parameters
<a name="API_GetAgentCard_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentRuntimeArn](#API_GetAgentCard_RequestSyntax) **   <a name="BedrockAgentCore-GetAgentCard-request-uri-agentRuntimeArn"></a>
The ARN of the AgentCore Runtime agent for which you want to get the A2A agent card.  
Required: Yes

 ** [qualifier](#API_GetAgentCard_RequestSyntax) **   <a name="BedrockAgentCore-GetAgentCard-request-uri-qualifier"></a>
Optional qualifier to specify an agent alias, such as `prod`code> or `dev`. If you don't provide a value, the DEFAULT alias is used. 

 ** [runtimeSessionId](#API_GetAgentCard_RequestSyntax) **   <a name="BedrockAgentCore-GetAgentCard-request-runtimeSessionId"></a>
The session ID that the AgentCore Runtime agent is using.   
Length Constraints: Minimum length of 33. Maximum length of 256.

## Request Body
<a name="API_GetAgentCard_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAgentCard_ResponseSyntax"></a>

```
HTTP/1.1 {{statusCode}}
X-Amzn-Bedrock-AgentCore-Runtime-Session-Id: {{runtimeSessionId}}
```

## Response Elements
<a name="API_GetAgentCard_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [statusCode](#API_GetAgentCard_ResponseSyntax) **   <a name="BedrockAgentCore-GetAgentCard-response-statusCode"></a>
The status code of the request.

The response returns the following HTTP headers.

 ** [runtimeSessionId](#API_GetAgentCard_ResponseSyntax) **   <a name="BedrockAgentCore-GetAgentCard-response-runtimeSessionId"></a>
The ID of the session associated with the AgentCore Runtime agent.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

## Errors
<a name="API_GetAgentCard_Errors"></a>

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
<a name="API_GetAgentCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetAgentCard) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetAgentCard) 