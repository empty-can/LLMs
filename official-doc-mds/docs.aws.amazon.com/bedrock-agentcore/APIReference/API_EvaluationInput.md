

# EvaluationInput
<a name="API_EvaluationInput"></a>

 The input data structure containing agent session spans in OpenTelemetry format. Supports traces from frameworks like Strands (AgentCore Runtime) and LangGraph with OpenInference instrumentation for comprehensive evaluation. 

## Contents
<a name="API_EvaluationInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** sessionSpans **   <a name="BedrockAgentCore-Type-EvaluationInput-sessionSpans"></a>
 The collection of spans representing agent execution traces within a session. Each span contains detailed information about tool calls, model interactions, and other agent activities that can be evaluated for quality and performance.   
Type: Array of JSON values  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Required: No

## See Also
<a name="API_EvaluationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/EvaluationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/EvaluationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/EvaluationInput) 