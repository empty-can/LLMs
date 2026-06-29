

# UpdateBrowserStream
<a name="API_UpdateBrowserStream"></a>

Updates a browser stream. To use this operation, you must have permissions to perform the bedrock:UpdateBrowserStream action.

## Request Syntax
<a name="API_UpdateBrowserStream_RequestSyntax"></a>

```
PUT /browsers/{{browserIdentifier}}/sessions/streams/update?sessionId={{sessionId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "streamUpdate": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateBrowserStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_UpdateBrowserStream_RequestSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-request-uri-browserIdentifier"></a>
The identifier of the browser.  
Required: Yes

 ** [sessionId](#API_UpdateBrowserStream_RequestSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-request-uri-sessionId"></a>
The identifier of the browser session.  
Pattern: `[0-9a-zA-Z]{1,40}`   
Required: Yes

## Request Body
<a name="API_UpdateBrowserStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateBrowserStream_RequestSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [streamUpdate](#API_UpdateBrowserStream_RequestSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-request-streamUpdate"></a>
The update to apply to the browser stream.  
Type: [StreamUpdate](API_StreamUpdate.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_UpdateBrowserStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "browserIdentifier": "string",
   "sessionId": "string",
   "streams": { 
      "automationStream": { 
         "streamEndpoint": "string",
         "streamStatus": "string"
      },
      "liveViewStream": { 
         "streamEndpoint": "string"
      }
   },
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateBrowserStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [browserIdentifier](#API_UpdateBrowserStream_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-response-browserIdentifier"></a>
The identifier of the browser.  
Type: String

 ** [sessionId](#API_UpdateBrowserStream_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-response-sessionId"></a>
The identifier of the browser session.  
Type: String  
Pattern: `[0-9a-zA-Z]{1,40}` 

 ** [streams](#API_UpdateBrowserStream_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-response-streams"></a>
The collection of streams associated with a browser session in Amazon Bedrock AgentCore. These streams provide different ways to interact with and observe the browser session, including programmatic control and visual representation of the browser content.  
Type: [BrowserSessionStream](API_BrowserSessionStream.md) object

 ** [updatedAt](#API_UpdateBrowserStream_ResponseSyntax) **   <a name="BedrockAgentCore-UpdateBrowserStream-response-updatedAt"></a>
The time at which the browser stream was updated.  
Type: Timestamp

## Errors
<a name="API_UpdateBrowserStream_Errors"></a>

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
<a name="API_UpdateBrowserStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/UpdateBrowserStream) 