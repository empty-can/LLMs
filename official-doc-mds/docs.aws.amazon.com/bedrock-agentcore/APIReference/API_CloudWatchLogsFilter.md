

# CloudWatchLogsFilter
<a name="API_CloudWatchLogsFilter"></a>

A filter for narrowing down agent traces from CloudWatch Logs based on key-value comparisons.

## Contents
<a name="API_CloudWatchLogsFilter_Contents"></a>

 ** key **   <a name="BedrockAgentCore-Type-CloudWatchLogsFilter-key"></a>
The key or field name to filter on within the agent trace data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9._-]+`   
Required: Yes

 ** operator **   <a name="BedrockAgentCore-Type-CloudWatchLogsFilter-operator"></a>
The comparison operator to use for filtering.  
Type: String  
Valid Values: `Equals | NotEquals | GreaterThan | LessThan | GreaterThanOrEqual | LessThanOrEqual | Contains | NotContains`   
Required: Yes

 ** value **   <a name="BedrockAgentCore-Type-CloudWatchLogsFilter-value"></a>
The value to compare against using the specified operator.  
Type: [FilterValue](API_FilterValue.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_CloudWatchLogsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchLogsFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchLogsFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchLogsFilter) 