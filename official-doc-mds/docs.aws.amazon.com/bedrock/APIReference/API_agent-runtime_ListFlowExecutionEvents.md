

# ListFlowExecutionEvents
<a name="API_agent-runtime_ListFlowExecutionEvents"></a>

Lists events that occurred during a flow execution. Events provide detailed information about the execution progress, including node inputs and outputs, flow inputs and outputs, condition results, and failure events.

**Note**  
Flow executions is in preview release for Amazon Bedrock and is subject to change.

## Request Syntax
<a name="API_agent-runtime_ListFlowExecutionEvents_RequestSyntax"></a>

```
GET /flows/{{flowIdentifier}}/aliases/{{flowAliasIdentifier}}/executions/{{executionIdentifier}}/events?eventType={{eventType}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_agent-runtime_ListFlowExecutionEvents_RequestParameters"></a>

The request uses the following URI parameters.

 ** [eventType](#API_agent-runtime_ListFlowExecutionEvents_RequestSyntax) **   <a name="bedrock-agent-runtime_ListFlowExecutionEvents-request-uri-eventType"></a>
The type of events to retrieve. Specify `Node` for node-level events or `Flow` for flow-level events.  
Valid Values: `Node | Flow`   
Required: Yes

 ** [executionIdentifier](#API_agent-runtime_ListFlowExecutionEvents_RequestSyntax) **   <a name="bedrock-agent-runtime_ListFlowExecutionEvents-request-uri-executionIdentifier"></a>
The unique identifier of the flow execution.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[a-zA-Z0-9-]{1,36}$|^(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10}/execution/[a-zA-Z0-9-]{1,36})`   
Required: Yes

 ** [flowAliasIdentifier](#API_agent-runtime_ListFlowExecutionEvents_RequestSyntax) **   <a name="bedrock-agent-runtime_ListFlowExecutionEvents-request-uri-flowAliasIdentifier"></a>
The unique identifier of the flow alias used for the execution.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}/alias/[0-9a-zA-Z]{10})|(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** [flowIdentifier](#API_agent-runtime_ListFlowExecutionEvents_RequestSyntax) **   <a name="bedrock-agent-runtime_ListFlowExecutionEvents-request-uri-flowIdentifier"></a>
The unique identifier of the flow.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

 ** [maxResults](#API_agent-runtime_ListFlowExecutionEvents_RequestSyntax) **   <a name="bedrock-agent-runtime_ListFlowExecutionEvents-request-uri-maxResults"></a>
The maximum number of events to return in a single response. If more events exist than the specified maxResults value, a token is included in the response so that the remaining results can be retrieved.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_agent-runtime_ListFlowExecutionEvents_RequestSyntax) **   <a name="bedrock-agent-runtime_ListFlowExecutionEvents-request-uri-nextToken"></a>
A token to retrieve the next set of results. This value is returned in the response if more results are available.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_agent-runtime_ListFlowExecutionEvents_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent-runtime_ListFlowExecutionEvents_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "flowExecutionEvents": [ 
      { ... }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_agent-runtime_ListFlowExecutionEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [flowExecutionEvents](#API_agent-runtime_ListFlowExecutionEvents_ResponseSyntax) **   <a name="bedrock-agent-runtime_ListFlowExecutionEvents-response-flowExecutionEvents"></a>
A list of events that occurred during the flow execution. Events can include node inputs and outputs, flow inputs and outputs, condition results, and failure events.  
Type: Array of [FlowExecutionEvent](API_agent-runtime_FlowExecutionEvent.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [nextToken](#API_agent-runtime_ListFlowExecutionEvents_ResponseSyntax) **   <a name="bedrock-agent-runtime_ListFlowExecutionEvents-response-nextToken"></a>
A token to retrieve the next set of results. This value is returned if more results are available.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_agent-runtime_ListFlowExecutionEvents_Errors"></a>

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

## See Also
<a name="API_agent-runtime_ListFlowExecutionEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/ListFlowExecutionEvents) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/ListFlowExecutionEvents) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ListFlowExecutionEvents) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/ListFlowExecutionEvents) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ListFlowExecutionEvents) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/ListFlowExecutionEvents) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/ListFlowExecutionEvents) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/ListFlowExecutionEvents) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/ListFlowExecutionEvents) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ListFlowExecutionEvents) 