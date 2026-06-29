

# ResponseStream
<a name="API_agent-runtime_ResponseStream"></a>

The response from invoking the agent and associated citations and trace information.

## Contents
<a name="API_agent-runtime_ResponseStream_Contents"></a>

 ** accessDeniedException **   <a name="bedrock-Type-agent-runtime_ResponseStream-accessDeniedException"></a>
The request is denied because of missing access permissions. Check your permissions and retry your request.  
Type: Exception  
HTTP Status Code: 403  
Required: No

 ** badGatewayException **   <a name="bedrock-Type-agent-runtime_ResponseStream-badGatewayException"></a>
There was an issue with a dependency due to a server issue. Retry your request.  
Type: Exception  
HTTP Status Code: 502  
Required: No

 ** chunk **   <a name="bedrock-Type-agent-runtime_ResponseStream-chunk"></a>
Contains a part of an agent response and citations for it.  
Type: [PayloadPart](API_agent-runtime_PayloadPart.md) object  
Required: No

 ** conflictException **   <a name="bedrock-Type-agent-runtime_ResponseStream-conflictException"></a>
There was a conflict performing an operation. Resolve the conflict and retry your request.  
Type: Exception  
HTTP Status Code: 409  
Required: No

 ** dependencyFailedException **   <a name="bedrock-Type-agent-runtime_ResponseStream-dependencyFailedException"></a>
There was an issue with a dependency. Check the resource configurations and retry the request.  
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** files **   <a name="bedrock-Type-agent-runtime_ResponseStream-files"></a>
Contains intermediate response for code interpreter if any files have been generated.  
Type: [FilePart](API_agent-runtime_FilePart.md) object  
Required: No

 ** internalServerException **   <a name="bedrock-Type-agent-runtime_ResponseStream-internalServerException"></a>
An internal server error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** modelNotReadyException **   <a name="bedrock-Type-agent-runtime_ResponseStream-modelNotReadyException"></a>
 The model specified in the request is not ready to serve Inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in the *AWS SDKs and Tools* reference guide.   
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** resourceNotFoundException **   <a name="bedrock-Type-agent-runtime_ResponseStream-resourceNotFoundException"></a>
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
Type: Exception  
HTTP Status Code: 404  
Required: No

 ** returnControl **   <a name="bedrock-Type-agent-runtime_ResponseStream-returnControl"></a>
Contains the parameters and information that the agent elicited from the customer to carry out an action. This information is returned to the system and can be used in your own setup for fulfilling the action.  
Type: [ReturnControlPayload](API_agent-runtime_ReturnControlPayload.md) object  
Required: No

 ** serviceQuotaExceededException **   <a name="bedrock-Type-agent-runtime_ResponseStream-serviceQuotaExceededException"></a>
The number of requests exceeds the service quota. Resubmit your request later.  
Type: Exception  
HTTP Status Code: 400  
Required: No

 ** throttlingException **   <a name="bedrock-Type-agent-runtime_ResponseStream-throttlingException"></a>
The number of requests exceeds the limit. Resubmit your request later.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** trace **   <a name="bedrock-Type-agent-runtime_ResponseStream-trace"></a>
Contains information about the agent and session, alongside the agent's reasoning process and results from calling actions and querying knowledge bases and metadata about the trace. You can use the trace to understand how the agent arrived at the response it provided the customer. For more information, see [Trace events](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html).  
Type: [TracePart](API_agent-runtime_TracePart.md) object  
Required: No

 ** validationException **   <a name="bedrock-Type-agent-runtime_ResponseStream-validationException"></a>
Input validation failed. Check your request parameters and retry the request.  
Type: Exception  
HTTP Status Code: 400  
Required: No

## See Also
<a name="API_agent-runtime_ResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ResponseStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ResponseStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ResponseStream) 