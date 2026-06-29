

# RootCauseCluster
<a name="API_RootCauseCluster"></a>

A cluster of similar root causes identified within a failure subcategory.

## Contents
<a name="API_RootCauseCluster_Contents"></a>

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-RootCauseCluster-affectedSessionCount"></a>
The number of sessions affected by this root cause.  
Type: Integer  
Required: Yes

 ** affectedSessions **   <a name="BedrockAgentCore-Type-RootCauseCluster-affectedSessions"></a>
The list of sessions affected by this root cause.  
Type: Array of [AffectedSession](API_AffectedSession.md) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

 ** clusterId **   <a name="BedrockAgentCore-Type-RootCauseCluster-clusterId"></a>
The unique identifier of the root cause cluster.  
Type: Integer  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-RootCauseCluster-name"></a>
The name of the root cause cluster.  
Type: String  
Required: Yes

 ** recommendation **   <a name="BedrockAgentCore-Type-RootCauseCluster-recommendation"></a>
The recommended fix for this root cause.  
Type: String  
Required: Yes

 ** rootCause **   <a name="BedrockAgentCore-Type-RootCauseCluster-rootCause"></a>
The root cause explanation for this cluster of failures.  
Type: String  
Required: Yes

## See Also
<a name="API_RootCauseCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RootCauseCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RootCauseCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RootCauseCluster) 