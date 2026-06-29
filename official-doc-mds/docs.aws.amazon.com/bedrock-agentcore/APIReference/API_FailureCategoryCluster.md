

# FailureCategoryCluster
<a name="API_FailureCategoryCluster"></a>

A top-level failure category identified by clustering similar failure patterns across sessions.

## Contents
<a name="API_FailureCategoryCluster_Contents"></a>

 ** affectedSessionCount **   <a name="BedrockAgentCore-Type-FailureCategoryCluster-affectedSessionCount"></a>
The number of sessions affected by this failure category.  
Type: Integer  
Required: Yes

 ** clusterId **   <a name="BedrockAgentCore-Type-FailureCategoryCluster-clusterId"></a>
The unique identifier of the failure category cluster.  
Type: Integer  
Required: Yes

 ** description **   <a name="BedrockAgentCore-Type-FailureCategoryCluster-description"></a>
A description of the failure category pattern.  
Type: String  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-FailureCategoryCluster-name"></a>
The name of the failure category.  
Type: String  
Required: Yes

 ** subCategories **   <a name="BedrockAgentCore-Type-FailureCategoryCluster-subCategories"></a>
The list of failure subcategories within this category.  
Type: Array of [FailureSubCategoryCluster](API_FailureSubCategoryCluster.md) objects  
Array Members: Minimum number of 0 items.  
Required: Yes

## See Also
<a name="API_FailureCategoryCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/FailureCategoryCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/FailureCategoryCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/FailureCategoryCluster) 