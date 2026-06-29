

# StartCodeInterpreterSession
<a name="API_StartCodeInterpreterSession"></a>

Creates and initializes a code interpreter session in Amazon Bedrock AgentCore. The session enables agents to execute code as part of their response generation, supporting programming languages such as Python for data analysis, visualization, and computation tasks.

To create a session, you must specify a code interpreter identifier and a name. The session remains active until it times out or you explicitly stop it using the `StopCodeInterpreterSession` operation.

The following operations are related to `StartCodeInterpreterSession`:
+  [InvokeCodeInterpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeCodeInterpreter.html) 
+  [GetCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html) 
+  [StopCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html) 

## Request Syntax
<a name="API_StartCodeInterpreterSession_RequestSyntax"></a>

```
PUT /code-interpreters/{{codeInterpreterIdentifier}}/sessions/start HTTP/1.1
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
Content-type: application/json

{
   "certificates": [ 
      { 
         "location": { ... }
      }
   ],
   "clientToken": "{{string}}",
   "name": "{{string}}",
   "sessionTimeoutSeconds": {{number}}
}
```

## URI Request Parameters
<a name="API_StartCodeInterpreterSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [codeInterpreterIdentifier](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-uri-codeInterpreterIdentifier"></a>
The unique identifier of the code interpreter to use for this session. This identifier specifies which code interpreter environment to initialize for the session.  
Required: Yes

 ** [traceId](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Request Body
<a name="API_StartCodeInterpreterSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificates](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-certificates"></a>
A list of certificates to install in the code interpreter session.  
Type: Array of [Certificate](API_Certificate.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [clientToken](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [name](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-name"></a>
The name of the code interpreter session. This name helps you identify and manage the session. The name does not need to be unique.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** [sessionTimeoutSeconds](#API_StartCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-request-sessionTimeoutSeconds"></a>
The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 900 seconds (15 minutes). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 28800.  
Required: No

## Response Syntax
<a name="API_StartCodeInterpreterSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "codeInterpreterIdentifier": "string",
   "createdAt": "string",
   "sessionId": "string"
}
```

## Response Elements
<a name="API_StartCodeInterpreterSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [codeInterpreterIdentifier](#API_StartCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-response-codeInterpreterIdentifier"></a>
The identifier of the code interpreter.  
Type: String

 ** [createdAt](#API_StartCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-response-createdAt"></a>
The time at which the code interpreter session was created.  
Type: Timestamp

 ** [sessionId](#API_StartCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartCodeInterpreterSession-response-sessionId"></a>
The unique identifier of the created code interpreter session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

## Errors
<a name="API_StartCodeInterpreterSession_Errors"></a>

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
<a name="API_StartCodeInterpreterSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StartCodeInterpreterSession) 