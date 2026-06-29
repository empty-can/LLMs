

# AgenticRetrieveStreamResponseOutput
<a name="API_agent-runtime_AgenticRetrieveStreamResponseOutput"></a>

The streaming output for agentic retrieval, containing results, traces, and errors.

## Contents
<a name="API_agent-runtime_AgenticRetrieveStreamResponseOutput_Contents"></a>

 ** accessDeniedException **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-accessDeniedException"></a>
Access to the resource was denied.  
Type: Exception  
HTTP Status Code: 403  
Required: No

 ** badGatewayException **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-badGatewayException"></a>
A bad gateway error occurred.  
Type: Exception  
HTTP Status Code: 502  
Required: No

 ** conflictException **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-conflictException"></a>
A conflict occurred with the current state of the resource.  
Type: Exception  
HTTP Status Code: 409  
Required: No

 ** dependencyFailedException **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-dependencyFailedException"></a>
A dependency failed during the operation.  
Type: Exception  
HTTP Status Code: 424  
Required: No

 ** internalServerException **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-internalServerException"></a>
An internal server error occurred.  
Type: Exception  
HTTP Status Code: 500  
Required: No

 ** resourceNotFoundException **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-resourceNotFoundException"></a>
The specified resource was not found.  
Type: Exception  
HTTP Status Code: 404  
Required: No

 ** responseEvent **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-responseEvent"></a>
A chunk of the generated answer. Emitted only when generateResponse is true.  
Type: [AgenticRetrieveResponseEvent](API_agent-runtime_AgenticRetrieveResponseEvent.md) object  
Required: No

 ** result **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-result"></a>
A retrieval result event containing the retrieved items.  
Type: [AgenticRetrieveResultEvent](API_agent-runtime_AgenticRetrieveResultEvent.md) object  
Required: No

 ** serviceQuotaExceededException **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-serviceQuotaExceededException"></a>
The service quota has been exceeded.  
Type: Exception  
HTTP Status Code: 400  
Required: No

 ** throttlingException **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-throttlingException"></a>
The request was throttled.  
Type: Exception  
HTTP Status Code: 429  
Required: No

 ** traceEvent **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-traceEvent"></a>
A trace event providing visibility into the retrieval process.  
Type: [AgenticRetrieveTraceEvent](API_agent-runtime_AgenticRetrieveTraceEvent.md) object  
Required: No

 ** validationException **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveStreamResponseOutput-validationException"></a>
The request validation failed.  
Type: Exception  
HTTP Status Code: 400  
Required: No

## See Also
<a name="API_agent-runtime_AgenticRetrieveStreamResponseOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStreamResponseOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStreamResponseOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveStreamResponseOutput) 