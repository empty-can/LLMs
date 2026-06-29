

# OnlineEvaluationConfigSummary
<a name="API_OnlineEvaluationConfigSummary"></a>

 The summary information about an online evaluation configuration, including basic metadata and execution status. 

## Contents
<a name="API_OnlineEvaluationConfigSummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-OnlineEvaluationConfigSummary-createdAt"></a>
 The timestamp when the online evaluation configuration was created.   
Type: Timestamp  
Required: Yes

 ** executionStatus **   <a name="bedrockagentcorecontrol-Type-OnlineEvaluationConfigSummary-executionStatus"></a>
 The execution status indicating whether the online evaluation is currently running.   
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

 ** onlineEvaluationConfigArn **   <a name="bedrockagentcorecontrol-Type-OnlineEvaluationConfigSummary-onlineEvaluationConfigArn"></a>
 The Amazon Resource Name (ARN) of the online evaluation configuration.   
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** onlineEvaluationConfigId **   <a name="bedrockagentcorecontrol-Type-OnlineEvaluationConfigSummary-onlineEvaluationConfigId"></a>
 The unique identifier of the online evaluation configuration.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** onlineEvaluationConfigName **   <a name="bedrockagentcorecontrol-Type-OnlineEvaluationConfigSummary-onlineEvaluationConfigName"></a>
 The name of the online evaluation configuration.   
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-OnlineEvaluationConfigSummary-status"></a>
 The status of the online evaluation configuration.   
Type: String  
Valid Values: `ACTIVE | CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | ERROR`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-OnlineEvaluationConfigSummary-updatedAt"></a>
 The timestamp when the online evaluation configuration was last updated.   
Type: Timestamp  
Required: Yes

 ** clusteringConfig **   <a name="bedrockagentcorecontrol-Type-OnlineEvaluationConfigSummary-clusteringConfig"></a>
The clustering configuration for periodic batch evaluation.  
Type: [ClusteringConfig](API_ClusteringConfig.md) object  
Required: No

 ** description **   <a name="bedrockagentcorecontrol-Type-OnlineEvaluationConfigSummary-description"></a>
 The description of the online evaluation configuration.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `.+`   
Required: No

 ** failureReason **   <a name="bedrockagentcorecontrol-Type-OnlineEvaluationConfigSummary-failureReason"></a>
 The reason for failure if the online evaluation configuration execution failed.   
Type: String  
Required: No

 ** insights **   <a name="bedrockagentcorecontrol-Type-OnlineEvaluationConfigSummary-insights"></a>
The list of insight types configured for this evaluation.  
Type: Array of [Insight](API_Insight.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

## See Also
<a name="API_OnlineEvaluationConfigSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/OnlineEvaluationConfigSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/OnlineEvaluationConfigSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/OnlineEvaluationConfigSummary) 