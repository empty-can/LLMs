

# GetCodeInterpreterSession
<a name="API_GetCodeInterpreterSession"></a>

Retrieves detailed information about a specific code interpreter session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, and metadata.

To get a code interpreter session, you must specify both the code interpreter identifier and the session ID. The response includes information about the session's timeout settings and current status.

The following operations are related to `GetCodeInterpreterSession`:
+  [StartCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html) 
+  [ListCodeInterpreterSessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListCodeInterpreterSessions.html) 
+  [StopCodeInterpreterSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html) 

## Request Syntax
<a name="API_GetCodeInterpreterSession_RequestSyntax"></a>

```
GET /code-interpreters/{{codeInterpreterIdentifier}}/sessions/get?sessionId={{sessionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCodeInterpreterSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [codeInterpreterIdentifier](#API_GetCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-request-uri-codeInterpreterIdentifier"></a>
The unique identifier of the code interpreter associated with the session.  
Required: Yes

 ** [sessionId](#API_GetCodeInterpreterSession_RequestSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-request-uri-sessionId"></a>
The unique identifier of the code interpreter session to retrieve.  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

## Request Body
<a name="API_GetCodeInterpreterSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCodeInterpreterSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificates": [ 
      { 
         "location": { ... }
      }
   ],
   "codeInterpreterIdentifier": "string",
   "createdAt": "string",
   "name": "string",
   "sessionId": "string",
   "sessionTimeoutSeconds": number,
   "status": "string"
}
```

## Response Elements
<a name="API_GetCodeInterpreterSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificates](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-certificates"></a>
The list of certificates installed in the code interpreter session.  
Type: Array of [Certificate](API_Certificate.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.

 ** [codeInterpreterIdentifier](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-codeInterpreterIdentifier"></a>
The identifier of the code interpreter.  
Type: String

 ** [createdAt](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-createdAt"></a>
The time at which the code interpreter session was created.  
Type: Timestamp

 ** [name](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-name"></a>
The name of the code interpreter session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [sessionId](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-sessionId"></a>
The identifier of the code interpreter session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

 ** [sessionTimeoutSeconds](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-sessionTimeoutSeconds"></a>
The timeout period for the code interpreter session in seconds.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 28800.

 ** [status](#API_GetCodeInterpreterSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetCodeInterpreterSession-response-status"></a>
The current status of the code interpreter session. Possible values include ACTIVE, STOPPING, and STOPPED.  
Type: String  
Valid Values: `READY | TERMINATED` 

## Errors
<a name="API_GetCodeInterpreterSession_Errors"></a>

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

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_GetCodeInterpreterSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetCodeInterpreterSession) 