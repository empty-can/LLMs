

# VersionLineageMetadata
<a name="API_VersionLineageMetadata"></a>

The version lineage metadata that tracks parent versions and creation source. Supports git-like two-parent merges for branch management.

## Contents
<a name="API_VersionLineageMetadata_Contents"></a>

 ** branchName **   <a name="bedrockagentcorecontrol-Type-VersionLineageMetadata-branchName"></a>
The branch name for this version. If not specified, inherits the parent's branch or defaults to `mainline`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z][a-zA-Z0-9_/-]{0,127}`   
Required: No

 ** commitMessage **   <a name="bedrockagentcorecontrol-Type-VersionLineageMetadata-commitMessage"></a>
A commit message describing the changes in this version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: No

 ** createdBy **   <a name="bedrockagentcorecontrol-Type-VersionLineageMetadata-createdBy"></a>
The source that created this version.  
Type: [VersionCreatedBySource](API_VersionCreatedBySource.md) object  
Required: No

 ** parentVersionIds **   <a name="bedrockagentcorecontrol-Type-VersionLineageMetadata-parentVersionIds"></a>
A list of parent version identifiers. Regular commits have 0-1 parents. Merge commits have 2 parents: the target branch parent and the source branch parent. The first parent represents the primary lineage.  
Type: Array of strings  
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: No

## See Also
<a name="API_VersionLineageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/VersionLineageMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/VersionLineageMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/VersionLineageMetadata) 