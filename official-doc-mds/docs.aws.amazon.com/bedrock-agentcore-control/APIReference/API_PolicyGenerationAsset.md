

# PolicyGenerationAsset
<a name="API_PolicyGenerationAsset"></a>

Represents a generated policy asset from the AI-powered policy generation process within the AgentCore Policy system. Each asset contains a Cedar policy statement generated from natural language input, along with associated metadata and analysis findings to help users evaluate and select the most appropriate policy option.

## Contents
<a name="API_PolicyGenerationAsset_Contents"></a>

 ** findings **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationAsset-findings"></a>
Analysis findings and insights related to this specific generated policy asset. These findings may include validation results, potential issues, or recommendations for improvement to help users evaluate the quality and appropriateness of the generated policy.  
Type: Array of [Finding](API_Finding.md) objects  
Required: Yes

 ** policyGenerationAssetId **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationAsset-policyGenerationAssetId"></a>
The unique identifier for this generated policy asset within the policy generation request. This ID can be used to reference specific generated policy options when creating actual policies from the generation results.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`   
Required: Yes

 ** rawTextFragment **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationAsset-rawTextFragment"></a>
The portion of the original natural language input that this generated policy asset addresses. This helps users understand which part of their policy description was translated into this specific Cedar policy statement, enabling better policy selection and refinement. When a single natural language input describes multiple authorization requirements, the generation process creates separate policy assets for each requirement, with each asset's rawTextFragment showing which requirement it addresses. Use this mapping to verify that all parts of your natural language input were correctly translated into Cedar policies.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: Yes

 ** definition **   <a name="bedrockagentcorecontrol-Type-PolicyGenerationAsset-definition"></a>
Represents the definition structure for policies within the AgentCore Policy system. This structure encapsulates different policy formats and languages that can be used to define access control rules.  
Type: [PolicyDefinition](API_PolicyDefinition.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_PolicyGenerationAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PolicyGenerationAsset) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PolicyGenerationAsset) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PolicyGenerationAsset) 