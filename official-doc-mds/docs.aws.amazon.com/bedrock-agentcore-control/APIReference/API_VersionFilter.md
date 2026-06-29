

# VersionFilter
<a name="API_VersionFilter"></a>

A filter for listing configuration bundle versions.

## Contents
<a name="API_VersionFilter_Contents"></a>

 ** branchName **   <a name="bedrockagentcorecontrol-Type-VersionFilter-branchName"></a>
Filter by branch name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z][a-zA-Z0-9_/-]{0,127}`   
Required: No

 ** createdByName **   <a name="bedrockagentcorecontrol-Type-VersionFilter-createdByName"></a>
Filter by creation source name.  
Type: String  
Required: No

 ** latestPerBranch **   <a name="bedrockagentcorecontrol-Type-VersionFilter-latestPerBranch"></a>
When true, returns only the latest version for each branch. When false or not specified, returns all versions. Can be combined with `branchName` to get the latest version for a specific branch.  
Type: Boolean  
Required: No

## See Also
<a name="API_VersionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/VersionFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/VersionFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/VersionFilter) 