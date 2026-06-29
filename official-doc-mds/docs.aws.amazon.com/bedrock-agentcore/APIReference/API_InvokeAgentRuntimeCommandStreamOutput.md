

# InvokeAgentRuntimeCommandStreamOutput
<a name="API_InvokeAgentRuntimeCommandStreamOutput"></a>

The streaming output union for the `InvokeAgentRuntimeCommand` operation. This union delivers typed events: `contentStart` (first), `contentDelta` (middle), and `contentStop` (last).

## Contents
<a name="API_InvokeAgentRuntimeCommandStreamOutput_Contents"></a>

 ** accessDeniedException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-accessDeniedException"></a>
Exception events for error streaming.  
Type: Exception  
HTTP Status Code: 403  
Required: No

 ** chunk **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-chunk"></a>
A response chunk containing command execution events such as content start, content delta, or content stop events.  
Type: [ResponseChunk](API_ResponseChunk.md) object  
Required: No

 ** internalServerException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** resourceNotFoundException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-resourceNotFoundException"></a>
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
Type: Exception  
HTTP Status Code: 404  
Required: No

 ** runtimeClientError **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-runtimeClientError"></a>
The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.  
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** serviceQuotaExceededException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-serviceQuotaExceededException"></a>
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
Type: Exception  
HTTP Status Code: 402  
Required: No

 ** throttlingException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-throttlingException"></a>
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** validationException **   <a name="BedrockAgentCore-Type-InvokeAgentRuntimeCommandStreamOutput-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
Type: Exception  
HTTP Status Code: 400  
Required: No

## See Also
<a name="API_InvokeAgentRuntimeCommandStreamOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandStreamOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandStreamOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeAgentRuntimeCommandStreamOutput) 