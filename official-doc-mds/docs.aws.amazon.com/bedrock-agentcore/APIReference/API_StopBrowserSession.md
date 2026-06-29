

# StopBrowserSession
<a name="API_StopBrowserSession"></a>

Terminates an active browser session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.

To stop a browser session, you must specify both the browser identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using `StartBrowserSession`.

The following operations are related to `StopBrowserSession`:
+  [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html) 
+  [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html) 

## Request Syntax
<a name="API_StopBrowserSession_RequestSyntax"></a>

```
PUT /browsers/{{browserIdentifier}}/sessions/stop?sessionId={{sessionId}} HTTP/1.1
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
Content-type: application/json

{
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopBrowserSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_StopBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-request-uri-browserIdentifier"></a>
The unique identifier of the browser associated with the session.  
Required: Yes

 ** [sessionId](#API_StopBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-request-uri-sessionId"></a>
The unique identifier of the browser session to stop.  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

 ** [traceId](#API_StopBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_StopBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Request Body
<a name="API_StopBrowserSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StopBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

## Response Syntax
<a name="API_StopBrowserSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserIdentifier": "string",
   "lastUpdatedAt": "string",
   "sessionId": "string"
}
```

## Response Elements
<a name="API_StopBrowserSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserIdentifier](#API_StopBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-response-browserIdentifier"></a>
The identifier of the browser.  
Type: String

 ** [lastUpdatedAt](#API_StopBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-response-lastUpdatedAt"></a>
The time at which the browser session was last updated.  
Type: Timestamp

 ** [sessionId](#API_StopBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StopBrowserSession-response-sessionId"></a>
The identifier of the browser session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

## Errors
<a name="API_StopBrowserSession_Errors"></a>

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
<a name="API_StopBrowserSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StopBrowserSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StopBrowserSession) 