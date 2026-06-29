

# BranchFilter
<a name="API_BranchFilter"></a>

Contains filter criteria for branches when listing events.

## Contents
<a name="API_BranchFilter_Contents"></a>

 ** name **   <a name="BedrockAgentCore-Type-BranchFilter-name"></a>
The name of the branch to filter by.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

 ** includeParentBranches **   <a name="BedrockAgentCore-Type-BranchFilter-includeParentBranches"></a>
Specifies whether to include parent branches in the results. Set to true to include parent branches, or false to exclude them.  
Type: Boolean  
Required: No

## See Also
<a name="API_BranchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/BranchFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/BranchFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/BranchFilter) 