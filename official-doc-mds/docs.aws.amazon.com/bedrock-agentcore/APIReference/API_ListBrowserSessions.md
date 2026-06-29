

# ListBrowserSessions
<a name="API_ListBrowserSessions"></a>

Retrieves a list of browser sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.

You can filter the results by browser identifier and session status. The operation supports pagination to handle large result sets efficiently.

We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.

The following operations are related to `ListBrowserSessions`:
+  [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html) 
+  [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html) 

## Request Syntax
<a name="API_ListBrowserSessions_RequestSyntax"></a>

```
POST /browsers/{{browserIdentifier}}/sessions/list HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListBrowserSessions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [browserIdentifier](#API_ListBrowserSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-request-uri-browserIdentifier"></a>
The unique identifier of the browser to list sessions for. If specified, only sessions for this browser are returned. If not specified, sessions for all browsers are returned.  
Required: Yes

## Request Body
<a name="API_ListBrowserSessions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListBrowserSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-request-maxResults"></a>
The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned `nextToken` value.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListBrowserSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

 ** [status](#API_ListBrowserSessions_RequestSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-request-status"></a>
The status of the browser sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.  
Type: String  
Valid Values: `READY | TERMINATED`   
Required: No

## Response Syntax
<a name="API_ListBrowserSessions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [ 
      { 
         "browserIdentifier": "string",
         "createdAt": "string",
         "lastUpdatedAt": "string",
         "name": "string",
         "sessionId": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBrowserSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListBrowserSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-response-items"></a>
The list of browser sessions that match the specified criteria.  
Type: Array of [BrowserSessionSummary](API_BrowserSessionSummary.md) objects

 ** [nextToken](#API_ListBrowserSessions_ResponseSyntax) **   <a name="BedrockAgentCore-ListBrowserSessions-response-nextToken"></a>
The token to use in a subsequent `ListBrowserSessions` request to get the next set of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListBrowserSessions_Errors"></a>

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
<a name="API_ListBrowserSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/ListBrowserSessions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ListBrowserSessions) 