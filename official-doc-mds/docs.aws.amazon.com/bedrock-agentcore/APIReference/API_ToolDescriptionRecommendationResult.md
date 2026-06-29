

# ToolDescriptionRecommendationResult
<a name="API_ToolDescriptionRecommendationResult"></a>

The result of a tool description recommendation, containing optimized descriptions.

## Contents
<a name="API_ToolDescriptionRecommendationResult_Contents"></a>

 ** configurationBundle **   <a name="BedrockAgentCore-Type-ToolDescriptionRecommendationResult-configurationBundle"></a>
The configuration bundle containing the recommended tool descriptions, if the input was sourced from a configuration bundle.  
Type: [RecommendationResultConfigurationBundle](API_RecommendationResultConfigurationBundle.md) object  
Required: No

 ** errorCode **   <a name="BedrockAgentCore-Type-ToolDescriptionRecommendationResult-errorCode"></a>
The error code if the recommendation failed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** errorMessage **   <a name="BedrockAgentCore-Type-ToolDescriptionRecommendationResult-errorMessage"></a>
The error message if the recommendation failed.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

 ** tools **   <a name="BedrockAgentCore-Type-ToolDescriptionRecommendationResult-tools"></a>
The list of tools with their recommended descriptions.  
Type: Array of [ToolDescriptionOutput](API_ToolDescriptionOutput.md) objects  
Required: No

## See Also
<a name="API_ToolDescriptionRecommendationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolDescriptionRecommendationResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolDescriptionRecommendationResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolDescriptionRecommendationResult) 