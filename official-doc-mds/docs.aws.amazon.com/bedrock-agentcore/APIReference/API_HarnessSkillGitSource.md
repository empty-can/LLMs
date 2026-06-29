

# HarnessSkillGitSource
<a name="API_HarnessSkillGitSource"></a>

A git repository source for a skill.

## Contents
<a name="API_HarnessSkillGitSource_Contents"></a>

 ** url **   <a name="BedrockAgentCore-Type-HarnessSkillGitSource-url"></a>
The HTTPS URL of the git repository.  
Type: String  
Length Constraints: Minimum length of 8.  
Pattern: `https://[^#@]+`   
Required: Yes

 ** auth **   <a name="BedrockAgentCore-Type-HarnessSkillGitSource-auth"></a>
Authentication configuration for private repositories.  
Type: [HarnessSkillGitAuth](API_HarnessSkillGitAuth.md) object  
Required: No

 ** path **   <a name="BedrockAgentCore-Type-HarnessSkillGitSource-path"></a>
Subdirectory within the repository containing the skill.  
Type: String  
Required: No

## See Also
<a name="API_HarnessSkillGitSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessSkillGitSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessSkillGitSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessSkillGitSource) 