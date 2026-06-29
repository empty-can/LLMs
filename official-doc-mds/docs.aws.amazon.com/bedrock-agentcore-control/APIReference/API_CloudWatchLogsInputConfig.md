

# CloudWatchLogsInputConfig
<a name="API_CloudWatchLogsInputConfig"></a>

 The configuration for reading agent traces from CloudWatch logs as input for online evaluation. 

## Contents
<a name="API_CloudWatchLogsInputConfig_Contents"></a>

 ** logGroupNames **   <a name="bedrockagentcorecontrol-Type-CloudWatchLogsInputConfig-logGroupNames"></a>
 The list of CloudWatch log group names to monitor for agent traces.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Pattern: `[.\-_/#A-Za-z0-9]+`   
Required: Yes

 ** serviceNames **   <a name="bedrockagentcorecontrol-Type-CloudWatchLogsInputConfig-serviceNames"></a>
 The list of service names to filter traces within the specified log groups. Used to identify relevant agent sessions.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9._-]+`   
Required: Yes

## See Also
<a name="API_CloudWatchLogsInputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CloudWatchLogsInputConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CloudWatchLogsInputConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CloudWatchLogsInputConfig) 