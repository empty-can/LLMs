

# PolicyGenerationDetails
<a name="API_PolicyGenerationDetails"></a>

Represents the information identifying a generated policy asset from the AI-powered policy generation process within the AgentCore Policy system. Each asset contains a Cedar policy statement generated from natural language input, along with associated metadata and analysis findings to help users evaluate and select the most appropriate policy option.

## Contents
<a name="API_PolicyGenerationDetails_Contents"></a>

 ** policyGenerationAssetId **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationDetails-policyGenerationAssetId"></a>
The unique identifier for this generated policy asset within the policy generation request.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** policyGenerationId **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationDetails-policyGenerationId"></a>
The unique identifier for this policy generation request.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

## See Also
<a name="API_PolicyGenerationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PolicyGenerationDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PolicyGenerationDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PolicyGenerationDetails) 