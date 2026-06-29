

# CustomConsolidationConfiguration
<a name="API_CustomConsolidationConfiguration"></a>

Contains custom consolidation configuration information.

## Contents
<a name="API_CustomConsolidationConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** episodicConsolidationOverride **   <a name="bedrockagentcorecontrol-Type-CustomConsolidationConfiguration-episodicConsolidationOverride"></a>
The configurations to override the default consolidation step for the episodic memory strategy.  
Type: [EpisodicConsolidationOverride](API_EpisodicConsolidationOverride.md) object  
Required: No

 ** semanticConsolidationOverride **   <a name="bedrockagentcorecontrol-Type-CustomConsolidationConfiguration-semanticConsolidationOverride"></a>
The semantic consolidation override configuration.  
Type: [SemanticConsolidationOverride](API_SemanticConsolidationOverride.md) object  
Required: No

 ** summaryConsolidationOverride **   <a name="bedrockagentcorecontrol-Type-CustomConsolidationConfiguration-summaryConsolidationOverride"></a>
The summary consolidation override configuration.  
Type: [SummaryConsolidationOverride](API_SummaryConsolidationOverride.md) object  
Required: No

 ** userPreferenceConsolidationOverride **   <a name="bedrockagentcorecontrol-Type-CustomConsolidationConfiguration-userPreferenceConsolidationOverride"></a>
The user preference consolidation override configuration.  
Type: [UserPreferenceConsolidationOverride](API_UserPreferenceConsolidationOverride.md) object  
Required: No

## See Also
<a name="API_CustomConsolidationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CustomConsolidationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CustomConsolidationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CustomConsolidationConfiguration) 