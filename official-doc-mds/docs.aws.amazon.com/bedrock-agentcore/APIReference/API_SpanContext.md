

# SpanContext
<a name="API_SpanContext"></a>

 The contextual information that uniquely identifies a span within the distributed tracing system. Contains session, trace, and span identifiers used to correlate evaluation results with specific agent execution points. 

## Contents
<a name="API_SpanContext_Contents"></a>

 ** sessionId **   <a name="BedrockAgentCore-Type-SpanContext-sessionId"></a>
 The unique identifier of the session containing this span. Sessions represent complete conversation flows and are detected using configurable `SessionTimeoutMinutes` (default 15 minutes).   
Type: String  
Required: Yes

 ** spanId **   <a name="BedrockAgentCore-Type-SpanContext-spanId"></a>
 The unique identifier of the specific span being referenced. Spans represent individual operations like tool calls, model invocations, or other discrete actions within the agent's execution.   
Type: String  
Required: No

 ** traceId **   <a name="BedrockAgentCore-Type-SpanContext-traceId"></a>
 The unique identifier of the trace containing this span. Traces represent individual request-response interactions within a session and group related spans together.   
Type: String  
Required: No

## See Also
<a name="API_SpanContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SpanContext) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SpanContext) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SpanContext) 