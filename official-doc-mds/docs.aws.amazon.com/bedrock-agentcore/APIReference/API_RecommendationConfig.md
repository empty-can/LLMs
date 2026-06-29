

# RecommendationConfig
<a name="API_RecommendationConfig"></a>

The configuration for a recommendation, varying by recommendation type.

## Contents
<a name="API_RecommendationConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** systemPromptRecommendationConfig **   <a name="BedrockAgentCore-Type-RecommendationConfig-systemPromptRecommendationConfig"></a>
The configuration for a system prompt recommendation.  
Type: [SystemPromptRecommendationConfig](API_SystemPromptRecommendationConfig.md) object  
Required: No

 ** toolDescriptionRecommendationConfig **   <a name="BedrockAgentCore-Type-RecommendationConfig-toolDescriptionRecommendationConfig"></a>
The configuration for a tool description recommendation.  
Type: [ToolDescriptionRecommendationConfig](API_ToolDescriptionRecommendationConfig.md) object  
Required: No

## See Also
<a name="API_RecommendationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RecommendationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RecommendationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RecommendationConfig) 