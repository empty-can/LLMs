

# ListInvocations
<a name="API_agent-runtime_ListInvocations"></a>

Lists all invocations associated with a specific session. For more information about sessions, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html).

## Request Syntax
<a name="API_agent-runtime_ListInvocations_RequestSyntax"></a>

```
POST /sessions/{{sessionIdentifier}}/invocations/?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent-runtime_ListInvocations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_agent-runtime_ListInvocations_RequestSyntax) **   <a name="bedrock-agent-runtime_ListInvocations-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_agent-runtime_ListInvocations_RequestSyntax) **   <a name="bedrock-agent-runtime_ListInvocations-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.   
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sessionIdentifier](#API_agent-runtime_ListInvocations_RequestSyntax) **   <a name="bedrock-agent-runtime_ListInvocations-request-uri-sessionIdentifier"></a>
The unique identifier for the session to list invocations for. You can specify either the session's `sessionId` or its Amazon Resource Name (ARN).  
Pattern: `(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]+:[0-9]{12}:session/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})|([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})`   
Required: Yes

## Request Body
<a name="API_agent-runtime_ListInvocations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent-runtime_ListInvocations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "invocationSummaries": [ 
      { 
         "createdAt": "string",
         "invocationId": "string",
         "sessionId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_agent-runtime_ListInvocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [invocationSummaries](#API_agent-runtime_ListInvocations_ResponseSyntax) **   <a name="bedrock-agent-runtime_ListInvocations-response-invocationSummaries"></a>
A list of invocation summaries associated with the session.  
Type: Array of [InvocationSummary](API_agent-runtime_InvocationSummary.md) objects

 ** [nextToken](#API_agent-runtime_ListInvocations_ResponseSyntax) **   <a name="bedrock-agent-runtime_ListInvocations-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_agent-runtime_ListInvocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_agent-runtime_ListInvocations_Examples"></a>

### Example request
<a name="API_agent-runtime_ListInvocations_Example_1"></a>

This example illustrates one usage of ListInvocations.

```
POST bedrock-agent-runtime.us-east-1.amazonaws.com/sessions/12345abc-1234-abcd-1234-abcdef123456/invocations/?maxResults=10&nextToken=abc123 HTTP/1.1
```

## See Also
<a name="API_agent-runtime_ListInvocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/ListInvocations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/ListInvocations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ListInvocations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/ListInvocations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ListInvocations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/ListInvocations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/ListInvocations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/ListInvocations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/ListInvocations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ListInvocations) 