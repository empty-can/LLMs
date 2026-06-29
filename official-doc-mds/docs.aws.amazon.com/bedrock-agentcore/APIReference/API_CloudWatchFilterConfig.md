

# CloudWatchFilterConfig
<a name="API_CloudWatchFilterConfig"></a>

Filter configuration for narrowing down CloudWatch Logs sessions for evaluation.

## Contents
<a name="API_CloudWatchFilterConfig_Contents"></a>

 ** sessionIds **   <a name="BedrockAgentCore-Type-CloudWatchFilterConfig-sessionIds"></a>
A list of specific session IDs to evaluate. If specified, only these sessions are included in the evaluation.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 500 items.  
Required: No

 ** timeRange **   <a name="BedrockAgentCore-Type-CloudWatchFilterConfig-timeRange"></a>
The time range filter for selecting sessions to evaluate.  
Type: [SessionFilterConfig](API_SessionFilterConfig.md) object  
Required: No

## See Also
<a name="API_CloudWatchFilterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchFilterConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchFilterConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchFilterConfig) 