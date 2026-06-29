

# ExecutionSummaryCluster
<a name="API_ExecutionSummaryCluster"></a>

A cluster of similar execution patterns identified across sessions.

## Contents
<a name="API_ExecutionSummaryCluster_Contents"></a>

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-ExecutionSummaryCluster-affectedSessionCount"></a>
The number of sessions with this execution pattern.  
Type: Integer  
Required: Yes

 ** affectedSessions **   <a name="BedrockAgentCore-Type-ExecutionSummaryCluster-affectedSessions"></a>
The list of sessions with this execution pattern.  
Type: Array of [ExecutionSummaryAffectedSession](API_ExecutionSummaryAffectedSession.md) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

 ** clusterId **   <a name="BedrockAgentCore-Type-ExecutionSummaryCluster-clusterId"></a>
The unique identifier of the execution summary cluster.  
Type: Integer  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-ExecutionSummaryCluster-description"></a>
A description of the execution pattern.  
Type: String  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-ExecutionSummaryCluster-name"></a>
The name of the execution pattern cluster.  
Type: String  
Required: Yes

## See Also
<a name="API_ExecutionSummaryCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExecutionSummaryCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExecutionSummaryCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExecutionSummaryCluster) 