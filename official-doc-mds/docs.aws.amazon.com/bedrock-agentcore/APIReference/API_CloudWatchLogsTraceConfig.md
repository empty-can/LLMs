

# CloudWatchLogsTraceConfig
<a name="API_CloudWatchLogsTraceConfig"></a>

Configuration for reading agent traces from CloudWatch Logs for recommendation analysis.

## Contents
<a name="API_CloudWatchLogsTraceConfig_Contents"></a>

 ** endTime **   <a name="BedrockAgentCore-Type-CloudWatchLogsTraceConfig-endTime"></a>
The end time of the time range to read traces from.  
Type: Timestamp  
Required: Yes

 ** logGroupArns **   <a name="BedrockAgentCore-Type-CloudWatchLogsTraceConfig-logGroupArns"></a>
The list of CloudWatch log group ARNs to read agent traces from.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: Yes

 ** serviceNames **   <a name="BedrockAgentCore-Type-CloudWatchLogsTraceConfig-serviceNames"></a>
The list of service names to filter traces within the specified log groups.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9._-]+`   
Required: Yes

 ** startTime **   <a name="BedrockAgentCore-Type-CloudWatchLogsTraceConfig-startTime"></a>
The start time of the time range to read traces from.  
Type: Timestamp  
Required: Yes

 ** rule **   <a name="BedrockAgentCore-Type-CloudWatchLogsTraceConfig-rule"></a>
Optional rule configuration for filtering traces.  
Type: [CloudWatchLogsRule](API_CloudWatchLogsRule.md) object  
Required: No

## See Also
<a name="API_CloudWatchLogsTraceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchLogsTraceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchLogsTraceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchLogsTraceConfig) 