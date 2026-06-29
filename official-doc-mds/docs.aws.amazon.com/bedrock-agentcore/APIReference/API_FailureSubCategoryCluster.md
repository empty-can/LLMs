

# FailureSubCategoryCluster
<a name="API_FailureSubCategoryCluster"></a>

A subcategory of failures within a top-level failure category.

## Contents
<a name="API_FailureSubCategoryCluster_Contents"></a>

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-FailureSubCategoryCluster-affectedSessionCount"></a>
The number of sessions affected by this failure subcategory.  
Type: Integer  
Required: Yes

 ** clusterId **   <a name="BedrockAgentCore-Type-FailureSubCategoryCluster-clusterId"></a>
The unique identifier of the failure subcategory cluster.  
Type: Integer  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-FailureSubCategoryCluster-description"></a>
A description of the failure subcategory pattern.  
Type: String  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-FailureSubCategoryCluster-name"></a>
The name of the failure subcategory.  
Type: String  
Required: Yes

 ** rootCauses **   <a name="BedrockAgentCore-Type-FailureSubCategoryCluster-rootCauses"></a>
The list of root cause clusters identified within this subcategory.  
Type: Array of [RootCauseCluster](API_RootCauseCluster.md) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

## See Also
<a name="API_FailureSubCategoryCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/FailureSubCategoryCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/FailureSubCategoryCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/FailureSubCategoryCluster) 