

# InvokeBrowser
<a name="API_InvokeBrowser"></a>

Invokes an operating system-level action on a browser session in Amazon Bedrock AgentCore. This operation provides direct OS-level control over browser sessions, enabling mouse actions, keyboard input, and screenshots that the WebSocket-based Chrome DevTools Protocol (CDP) cannot handle — such as interacting with print dialogs, context menus, and JavaScript alerts.

You send a request with exactly one action in the `BrowserAction` union, and receive a corresponding result in the `BrowserActionResult` union.

The following operations are related to `InvokeBrowser`:
+  [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html) 
+  [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html) 
+  [StopBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html) 

## Request Syntax
<a name="API_InvokeBrowser_RequestSyntax"></a>

```
POST /browsers/{{browserIdentifier}}/sessions/invoke HTTP/1.1
x-amzn-browser-session-id: {{sessionId}}
Content-type: application/json

{
   "action": { ... }
}
```

## URI Request Parameters
<a name="API_InvokeBrowser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_InvokeBrowser_RequestSyntax) **   <a name="BedrockAgentCore-InvokeBrowser-request-uri-browserIdentifier"></a>
The unique identifier of the browser associated with the session. This must match the identifier used when creating the session with `StartBrowserSession`.  
Required: Yes

 ** [sessionId](#API_InvokeBrowser_RequestSyntax) **   <a name="BedrockAgentCore-InvokeBrowser-request-sessionId"></a>
The unique identifier of the browser session on which to perform the action. This must be an active session created with `StartBrowserSession`.  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

## Request Body
<a name="API_InvokeBrowser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_InvokeBrowser_RequestSyntax) **   <a name="BedrockAgentCore-InvokeBrowser-request-action"></a>
The browser action to perform. Exactly one member of the `BrowserAction` union must be set per request.  
Type: [BrowserAction](API_BrowserAction.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_InvokeBrowser_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amzn-browser-session-id: {{sessionId}}
Content-type: application/json

{
   "result": { ... }
}
```

## Response Elements
<a name="API_InvokeBrowser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [sessionId](#API_InvokeBrowser_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeBrowser-response-sessionId"></a>
The unique identifier of the browser session on which the action was performed.  
Pattern: `[0-9a-zA-Z]{1,40}` 

The following data is returned in JSON format by the service.

 ** [result](#API_InvokeBrowser_ResponseSyntax) **   <a name="BedrockAgentCore-InvokeBrowser-response-result"></a>
The result of the browser action. The member set in the result corresponds to the action that was performed.  
Type: [BrowserActionResult](API_BrowserActionResult.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_InvokeBrowser_Errors"></a>

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
<a name="API_InvokeBrowser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/InvokeBrowser) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeBrowser) 