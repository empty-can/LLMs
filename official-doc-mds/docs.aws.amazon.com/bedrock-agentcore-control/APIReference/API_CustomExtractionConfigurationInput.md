

# CustomExtractionConfigurationInput
<a name="API_CustomExtractionConfigurationInput"></a>

Input for a custom extraction configuration.

## Contents
<a name="API_CustomExtractionConfigurationInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** episodicExtractionOverride **   <a name="bedrockagentcorecontrol-Type-CustomExtractionConfigurationInput-episodicExtractionOverride"></a>
Configurations to override the extraction step of the episodic strategy.  
Type: [EpisodicOverrideExtractionConfigurationInput](API_EpisodicOverrideExtractionConfigurationInput.md) object  
Required: No

 ** semanticExtractionOverride **   <a name="bedrockagentcorecontrol-Type-CustomExtractionConfigurationInput-semanticExtractionOverride"></a>
The semantic extraction override configuration input.  
Type: [SemanticOverrideExtractionConfigurationInput](API_SemanticOverrideExtractionConfigurationInput.md) object  
Required: No

 ** userPreferenceExtractionOverride **   <a name="bedrockagentcorecontrol-Type-CustomExtractionConfigurationInput-userPreferenceExtractionOverride"></a>
The user preference extraction override configuration input.  
Type: [UserPreferenceOverrideExtractionConfigurationInput](API_UserPreferenceOverrideExtractionConfigurationInput.md) object  
Required: No

## See Also
<a name="API_CustomExtractionConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CustomExtractionConfigurationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CustomExtractionConfigurationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CustomExtractionConfigurationInput) 