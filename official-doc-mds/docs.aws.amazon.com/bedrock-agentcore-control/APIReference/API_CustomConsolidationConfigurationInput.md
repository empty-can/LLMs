

# CustomConsolidationConfigurationInput
<a name="API_CustomConsolidationConfigurationInput"></a>

Input for a custom consolidation configuration.

## Contents
<a name="API_CustomConsolidationConfigurationInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** episodicConsolidationOverride **   <a name="bedrockagentcorecontrol-Type-CustomConsolidationConfigurationInput-episodicConsolidationOverride"></a>
Configurations to override the consolidation step of the episodic strategy.  
Type: [EpisodicOverrideConsolidationConfigurationInput](API_EpisodicOverrideConsolidationConfigurationInput.md) object  
Required: No

 ** semanticConsolidationOverride **   <a name="bedrockagentcorecontrol-Type-CustomConsolidationConfigurationInput-semanticConsolidationOverride"></a>
The semantic consolidation override configuration input.  
Type: [SemanticOverrideConsolidationConfigurationInput](API_SemanticOverrideConsolidationConfigurationInput.md) object  
Required: No

 ** summaryConsolidationOverride **   <a name="bedrockagentcorecontrol-Type-CustomConsolidationConfigurationInput-summaryConsolidationOverride"></a>
The summary consolidation override configuration input.  
Type: [SummaryOverrideConsolidationConfigurationInput](API_SummaryOverrideConsolidationConfigurationInput.md) object  
Required: No

 ** userPreferenceConsolidationOverride **   <a name="bedrockagentcorecontrol-Type-CustomConsolidationConfigurationInput-userPreferenceConsolidationOverride"></a>
The user preference consolidation override configuration input.  
Type: [UserPreferenceOverrideConsolidationConfigurationInput](API_UserPreferenceOverrideConsolidationConfigurationInput.md) object  
Required: No

## See Also
<a name="API_CustomConsolidationConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CustomConsolidationConfigurationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CustomConsolidationConfigurationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CustomConsolidationConfigurationInput) 