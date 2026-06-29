

# DataSourceConfig
<a name="API_DataSourceConfig"></a>

Configuration for the data source used in evaluation.

## Contents
<a name="API_DataSourceConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cloudWatchLogs **   <a name="BedrockAgentCore-Type-DataSourceConfig-cloudWatchLogs"></a>
Configuration for pulling agent session traces from CloudWatch Logs.  
Type: [CloudWatchLogsSource](API_CloudWatchLogsSource.md) object  
Required: No

 ** onlineEvaluationConfigSource **   <a name="BedrockAgentCore-Type-DataSourceConfig-onlineEvaluationConfigSource"></a>
A reference to an existing online evaluation configuration to use as the data source for batch evaluation.  
Type: [OnlineEvaluationConfigSource](API_OnlineEvaluationConfigSource.md) object  
Required: No

## See Also
<a name="API_DataSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DataSourceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DataSourceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DataSourceConfig) 