

# CustomExtractionConfiguration
<a name="API_CustomExtractionConfiguration"></a>

Contains custom extraction configuration information.

## Contents
<a name="API_CustomExtractionConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** episodicExtractionOverride **   <a name="bedrockagentcorecontrol-Type-CustomExtractionConfiguration-episodicExtractionOverride"></a>
The configurations to override the default extraction step for the episodic memory strategy.  
Type: [EpisodicExtractionOverride](API_EpisodicExtractionOverride.md) object  
Required: No

 ** semanticExtractionOverride **   <a name="bedrockagentcorecontrol-Type-CustomExtractionConfiguration-semanticExtractionOverride"></a>
The semantic extraction override configuration.  
Type: [SemanticExtractionOverride](API_SemanticExtractionOverride.md) object  
Required: No

 ** userPreferenceExtractionOverride **   <a name="bedrockagentcorecontrol-Type-CustomExtractionConfiguration-userPreferenceExtractionOverride"></a>
The user preference extraction override configuration.  
Type: [UserPreferenceExtractionOverride](API_UserPreferenceExtractionOverride.md) object  
Required: No

## See Also
<a name="API_CustomExtractionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CustomExtractionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CustomExtractionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CustomExtractionConfiguration) 