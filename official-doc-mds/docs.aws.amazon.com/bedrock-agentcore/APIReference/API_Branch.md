

# Branch
<a name="API_Branch"></a>

Contains information about a branch in an AgentCore Memory resource. Branches allow for organizing events into different conversation threads or paths.

## Contents
<a name="API_Branch_Contents"></a>

 ** name **   <a name="BedrockAgentCore-Type-Branch-name"></a>
The name of the branch.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

 ** rootEventId **   <a name="BedrockAgentCore-Type-Branch-rootEventId"></a>
The identifier of the root event for this branch.  
Type: String  
Pattern: `[0-9]+#[a-fA-F0-9]+`   
Required: No

## See Also
<a name="API_Branch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Branch) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Branch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Branch) 