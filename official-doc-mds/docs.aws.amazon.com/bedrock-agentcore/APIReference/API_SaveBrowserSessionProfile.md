

# SaveBrowserSessionProfile
<a name="API_SaveBrowserSessionProfile"></a>

Saves the current state of a browser session as a reusable profile in Amazon Bedrock AgentCore. A browser profile captures persistent browser data such as cookies and local storage from an active session, enabling you to reuse this data in future browser sessions.

To save a browser session profile, you must specify the profile identifier, browser identifier, and session ID. The session must be active when saving the profile. Once saved, the profile can be used with the `StartBrowserSession` operation to initialize new sessions with the stored browser state.

Browser profiles are useful for scenarios that require persistent authentication, maintaining user preferences across sessions, or continuing tasks that depend on previously stored browser data.

The following operations are related to `SaveBrowserSessionProfile`:
+  [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html) 
+  [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html) 

## Request Syntax
<a name="API_SaveBrowserSessionProfile_RequestSyntax"></a>

```
PUT /browser-profiles/{{profileIdentifier}}/save HTTP/1.1
X-Amzn-Trace-Id: {{traceId}}
traceparent: {{traceParent}}
Content-type: application/json

{
   "browserIdentifier": "{{string}}",
   "clientToken": "{{string}}",
   "sessionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SaveBrowserSessionProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [profileIdentifier](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-uri-profileIdentifier"></a>
The unique identifier for the browser profile. This identifier is used to reference the profile when starting new browser sessions. The identifier must follow the pattern of an alphanumeric name (up to 48 characters) followed by a hyphen and a 10-character alphanumeric suffix.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [traceId](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-traceId"></a>
The trace identifier for request tracking.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [traceParent](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-traceParent"></a>
The parent trace information for distributed tracing.  
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Request Body
<a name="API_SaveBrowserSessionProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [browserIdentifier](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-browserIdentifier"></a>
The unique identifier of the browser associated with the session from which to save the profile.  
Type: String  
Required: Yes

 ** [clientToken](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [sessionId](#API_SaveBrowserSessionProfile_RequestSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-request-sessionId"></a>
The unique identifier of the browser session from which to save the profile. The session must be active when saving the profile.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

## Response Syntax
<a name="API_SaveBrowserSessionProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserIdentifier": "string",
   "lastUpdatedAt": "string",
   "profileIdentifier": "string",
   "sessionId": "string"
}
```

## Response Elements
<a name="API_SaveBrowserSessionProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserIdentifier](#API_SaveBrowserSessionProfile_ResponseSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-response-browserIdentifier"></a>
The unique identifier of the browser associated with the session from which the profile was saved.  
Type: String

 ** [lastUpdatedAt](#API_SaveBrowserSessionProfile_ResponseSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-response-lastUpdatedAt"></a>
The timestamp when the browser profile was last updated. This value is in ISO 8601 format.  
Type: Timestamp

 ** [profileIdentifier](#API_SaveBrowserSessionProfile_ResponseSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-response-profileIdentifier"></a>
The unique identifier of the saved browser profile.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [sessionId](#API_SaveBrowserSessionProfile_ResponseSyntax) **   <a name="BedrockAgentCore-SaveBrowserSessionProfile-response-sessionId"></a>
The unique identifier of the browser session from which the profile was saved.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

## Errors
<a name="API_SaveBrowserSessionProfile_Errors"></a>

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

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_SaveBrowserSessionProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SaveBrowserSessionProfile) 