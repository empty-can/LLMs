

# AgentTracesConfig
<a name="API_AgentTracesConfig"></a>

The configuration specifying where to read agent traces from for recommendation analysis.

## Contents
<a name="API_AgentTracesConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** batchEvaluation **   <a name="BedrockAgentCore-Type-AgentTracesConfig-batchEvaluation"></a>
Use a completed batch evaluation as the source of agent traces.  
Type: [BatchEvaluationTraceConfig](API_BatchEvaluationTraceConfig.md) object  
Required: No

 ** cloudwatchLogs **   <a name="BedrockAgentCore-Type-AgentTracesConfig-cloudwatchLogs"></a>
Agent traces read from CloudWatch Logs.  
Type: [CloudWatchLogsTraceConfig](API_CloudWatchLogsTraceConfig.md) object  
Required: No

 ** sessionSpans **   <a name="BedrockAgentCore-Type-AgentTracesConfig-sessionSpans"></a>
Agent traces provided as inline session spans in OpenTelemetry format.  
Type: Array of JSON values  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Required: No

## See Also
<a name="API_AgentTracesConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/AgentTracesConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/AgentTracesConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/AgentTracesConfig) 