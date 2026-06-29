

# GetBrowserSession
<a name="API_GetBrowserSession"></a>

Retrieves detailed information about a specific browser session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, associated streams, and metadata.

To get a browser session, you must specify both the browser identifier and the session ID. The response includes information about the session's viewport configuration, timeout settings, and stream endpoints.

The following operations are related to `GetBrowserSession`:
+  [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html) 
+  [ListBrowserSessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListBrowserSessions.html) 
+  [StopBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html) 

## Request Syntax
<a name="API_GetBrowserSession_RequestSyntax"></a>

```
GET /browsers/{{browserIdentifier}}/sessions/get?sessionId={{sessionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBrowserSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_GetBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-request-uri-browserIdentifier"></a>
The unique identifier of the browser associated with the session.  
Required: Yes

 ** [sessionId](#API_GetBrowserSession_RequestSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-request-uri-sessionId"></a>
The unique identifier of the browser session to retrieve.  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

## Request Body
<a name="API_GetBrowserSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBrowserSession_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserIdentifier": "string",
   "certificates": [ 
      { 
         "location": { ... }
      }
   ],
   "createdAt": "string",
   "enterprisePolicies": [ 
      { 
         "location": { ... },
         "type": "string"
      }
   ],
   "extensions": [ 
      { 
         "location": { ... }
      }
   ],
   "lastUpdatedAt": "string",
   "name": "string",
   "profileConfiguration": { 
      "profileIdentifier": "string"
   },
   "proxyConfiguration": { 
      "bypass": { 
         "domainPatterns": [ "string" ]
      },
      "proxies": [ 
         { ... }
      ]
   },
   "sessionId": "string",
   "sessionReplayArtifact": "string",
   "sessionTimeoutSeconds": number,
   "status": "string",
   "streams": { 
      "automationStream": { 
         "streamEndpoint": "string",
         "streamStatus": "string"
      },
      "liveViewStream": { 
         "streamEndpoint": "string"
      }
   },
   "viewPort": { 
      "height": number,
      "width": number
   }
}
```

## Response Elements
<a name="API_GetBrowserSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserIdentifier](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-browserIdentifier"></a>
The identifier of the browser.  
Type: String

 ** [certificates](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-certificates"></a>
The list of certificates installed in the browser session.  
Type: Array of [Certificate](API_Certificate.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.

 ** [createdAt](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-createdAt"></a>
The time at which the browser session was created.  
Type: Timestamp

 ** [enterprisePolicies](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-enterprisePolicies"></a>
A list of files containing enterprise policies for the browser session.  
Type: Array of [BrowserEnterprisePolicy](API_BrowserEnterprisePolicy.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [extensions](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-extensions"></a>
The list of browser extensions that are configured in the browser session.  
Type: Array of [BrowserExtension](API_BrowserExtension.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [lastUpdatedAt](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-lastUpdatedAt"></a>
The time at which the browser session was last updated.  
Type: Timestamp

 ** [name](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-name"></a>
The name of the browser session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [profileConfiguration](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-profileConfiguration"></a>
The browser profile configuration associated with this session. Contains the profile identifier that links to persistent browser data such as cookies and local storage.  
Type: [BrowserProfileConfiguration](API_BrowserProfileConfiguration.md) object

 ** [proxyConfiguration](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-proxyConfiguration"></a>
The active proxy configuration for this browser session. This field is only present if proxy configuration was provided when the session was started using `StartBrowserSession`. The configuration includes proxy servers, domain bypass rules and the proxy authentication credentials.  
Type: [ProxyConfiguration](API_ProxyConfiguration.md) object

 ** [sessionId](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-sessionId"></a>
The identifier of the browser session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

 ** [sessionReplayArtifact](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-sessionReplayArtifact"></a>
The artifact containing the session replay information.  
Type: String

 ** [sessionTimeoutSeconds](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-sessionTimeoutSeconds"></a>
The timeout period for the browser session in seconds.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 28800.

 ** [status](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-status"></a>
The current status of the browser session. Possible values include ACTIVE, STOPPING, and STOPPED.  
Type: String  
Valid Values: `READY | TERMINATED` 

 ** [streams](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-streams"></a>
The streams associated with this browser session. These include the automation stream and live view stream.  
Type: [BrowserSessionStream](API_BrowserSessionStream.md) object

 ** [viewPort](#API_GetBrowserSession_ResponseSyntax) **   <a name="BedrockAgentCore-GetBrowserSession-response-viewPort"></a>
The configuration that defines the dimensions of a browser viewport in a browser session. The viewport determines the visible area of web content and affects how web pages are rendered and displayed. Proper viewport configuration ensures that web content is displayed correctly for the agent's browsing tasks.  
Type: [ViewPort](API_ViewPort.md) object

## Errors
<a name="API_GetBrowserSession_Errors"></a>

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
<a name="API_GetBrowserSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/GetBrowserSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/GetBrowserSession) 