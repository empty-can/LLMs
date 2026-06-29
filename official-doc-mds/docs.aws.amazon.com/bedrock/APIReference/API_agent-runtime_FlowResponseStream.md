

# FlowResponseStream
<a name="API_agent-runtime_FlowResponseStream"></a>

The output of the flow.

## Contents
<a name="API_agent-runtime_FlowResponseStream_Contents"></a>

 ** accessDeniedException **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-accessDeniedException"></a>
The request is denied because of missing access permissions. Check your permissions and retry your request.  
Type: Exception  
HTTP Status Code: 403  
Required: No

 ** badGatewayException **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-badGatewayException"></a>
There was an issue with a dependency due to a server issue. Retry your request.  
Type: Exception  
HTTP Status Code: 502  
Required: No

 ** conflictException **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-conflictException"></a>
There was a conflict performing an operation. Resolve the conflict and retry your request.  
Type: Exception  
HTTP Status Code: 409  
Required: No

 ** dependencyFailedException **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-dependencyFailedException"></a>
There was an issue with a dependency. Check the resource configurations and retry the request.  
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** flowCompletionEvent **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-flowCompletionEvent"></a>
Contains information about why the flow completed.  
Type: [FlowCompletionEvent](API_agent-runtime_FlowCompletionEvent.md) object  
Required: No

 ** flowMultiTurnInputRequestEvent **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-flowMultiTurnInputRequestEvent"></a>
The event stream containing the multi-turn input request information from the flow.  
Type: [FlowMultiTurnInputRequestEvent](API_agent-runtime_FlowMultiTurnInputRequestEvent.md) object  
Required: No

 ** flowOutputEvent **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-flowOutputEvent"></a>
Contains information about an output from flow invocation.  
Type: [FlowOutputEvent](API_agent-runtime_FlowOutputEvent.md) object  
Required: No

 ** flowTraceEvent **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-flowTraceEvent"></a>
Contains information about a trace, which tracks an input or output for a node in the flow.  
Type: [FlowTraceEvent](API_agent-runtime_FlowTraceEvent.md) object  
Required: No

 ** internalServerException **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-internalServerException"></a>
An internal server error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** resourceNotFoundException **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-resourceNotFoundException"></a>
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
Type: Exception  
HTTP Status Code: 404  
Required: No

 ** serviceQuotaExceededException **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-serviceQuotaExceededException"></a>
The number of requests exceeds the service quota. Resubmit your request later.  
Type: Exception  
HTTP Status Code: 400  
Required: No

 ** throttlingException **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-throttlingException"></a>
The number of requests exceeds the limit. Resubmit your request later.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** validationException **   <a name="bedrock-Type-agent-runtime_FlowResponseStream-validationException"></a>
Input validation failed. Check your request parameters and retry the request.  
Type: Exception  
HTTP Status Code: 400  
Required: No

## See Also
<a name="API_agent-runtime_FlowResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FlowResponseStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FlowResponseStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FlowResponseStream) 