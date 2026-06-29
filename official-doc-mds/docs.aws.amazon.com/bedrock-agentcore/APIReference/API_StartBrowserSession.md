

# StartBrowserSession
<a name="API_StartBrowserSession"></a>

Creates and initializes a browser session in Amazon Bedrock AgentCore. The session enables agents to navigate and interact with web content, extract information from websites, and perform web-based tasks as part of their response generation.

To create a session, you must specify a browser identifier and a name. You can also configure the viewport dimensions to control the visible area of web content. The session remains active until it times out or you explicitly stop it using the `StopBrowserSession` operation.

The following operations are related to `StartBrowserSession`:
+  [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html) 
+  [UpdateBrowserStream](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UpdateBrowserStream.html) 
+  [SaveBrowserSessionProfile](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SaveBrowserSessionProfile.html) 
+  [StopBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html) 
+  [InvokeBrowser](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeBrowser.html) 

## Request Syntax
<a name="API_StartBrowserSession_RequestSyntax"></a>

```
PUT /browsers/{{browserIdentifier}}/sessions/start HTTP/1.1
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
   "enterprisePolicies": [ 
      { 
         "location": { ... },
         "type": "{{string}}"
      }
   ],
   "extensions": [ 
      { 
         "location": { ... }
      }
   ],
   "name": "{{string}}",
   "profileConfiguration": { 
      "profileIdentifier": "{{string}}"
   },
   "proxyConfiguration": { 
      "bypass": { 
         "domainPatterns": [ "{{string}}" ]
      },
      "proxies": [ 
         { ... }
      ]
   },
   "sessionTimeoutSeconds": {{number}},
   "viewPort": { 
      "height": {{number}},
      "width": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_StartBrowserSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-uri-browserIdentifier"></a>
The unique identifier of the browser to use for this session. This identifier specifies which browser environment to initialize for the session.  
Required: Yes

 ** [traceId](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Request Body
<a name="API_StartBrowserSession_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificates](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-certificates"></a>
A list of certificates to install in the browser session.  
Type: Array of [Certificate](API_Certificate.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [clientToken](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [enterprisePolicies](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-enterprisePolicies"></a>
A list of files containing enterprise policies for the browser.  
Type: Array of [BrowserEnterprisePolicy](API_BrowserEnterprisePolicy.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: No

 ** [extensions](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-extensions"></a>
A list of browser extensions to load into the browser session.  
Type: Array of [BrowserExtension](API_BrowserExtension.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** [name](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-name"></a>
The name of the browser session. This name helps you identify and manage the session. The name does not need to be unique.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** [profileConfiguration](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-profileConfiguration"></a>
The browser profile configuration to use for this session. A browser profile contains persistent data such as cookies and local storage that can be reused across multiple browser sessions. If specified, the session initializes with the profile's stored data, enabling continuity for tasks that require authentication or personalized settings.  
Type: [BrowserProfileConfiguration](API_BrowserProfileConfiguration.md) object  
Required: No

 ** [proxyConfiguration](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-proxyConfiguration"></a>
Optional proxy configuration for routing browser traffic through customer-specified proxy servers. When provided, enables HTTP Basic authentication via AWS Secrets Manager and domain-based routing rules. Requires `secretsmanager:GetSecretValue` IAM permission for the specified secret ARNs.  
Type: [ProxyConfiguration](API_ProxyConfiguration.md) object  
Required: No

 ** [sessionTimeoutSeconds](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-sessionTimeoutSeconds"></a>
The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 3600 seconds (1 hour). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 28800.  
Required: No

 ** [viewPort](#API_StartBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-request-viewPort"></a>
The dimensions of the browser viewport for this session. This determines the visible area of the web content and affects how web pages are rendered. If not specified, Amazon Bedrock AgentCore uses a default viewport size.  
Type: [ViewPort](API_ViewPort.md) object  
Required: No

## Response Syntax
<a name="API_StartBrowserSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserIdentifier": "string",
   "createdAt": "string",
   "sessionId": "string",
   "streams": { 
      "automationStream": { 
         "streamEndpoint": "string",
         "streamStatus": "string"
      },
      "liveViewStream": { 
         "streamEndpoint": "string"
      }
   }
}
```

## Response Elements
<a name="API_StartBrowserSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserIdentifier](#API_StartBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-response-browserIdentifier"></a>
The identifier of the browser.  
Type: String

 ** [createdAt](#API_StartBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-response-createdAt"></a>
The timestamp when the browser session was created.  
Type: Timestamp

 ** [sessionId](#API_StartBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-response-sessionId"></a>
The unique identifier of the created browser session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

 ** [streams](#API_StartBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-StartBrowserSession-response-streams"></a>
The streams associated with this browser session. These include the automation stream and live view stream.  
Type: [BrowserSessionStream](API_BrowserSessionStream.md) object

## Errors
<a name="API_StartBrowserSession_Errors"></a>

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
<a name="API_StartBrowserSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/StartBrowserSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/StartBrowserSession) 