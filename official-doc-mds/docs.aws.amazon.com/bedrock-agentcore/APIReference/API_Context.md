

# Context
<a name="API_Context"></a>

 The contextual information associated with an evaluation, including span context details that identify the specific traces and sessions being evaluated within the agent's execution flow. 

## Contents
<a name="API_Context_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** spanContext **   <a name="BedrockAgentCore-Type-Context-spanContext"></a>
 The span context information that uniquely identifies the trace and span being evaluated, including session ID, trace ID, and span ID for precise targeting within the agent's execution flow.   
Type: [SpanContext](API_SpanContext.md) object  
Required: No

## See Also
<a name="API_Context_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Context) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Context) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Context) 