

# CustomConfigurationInput
<a name="API_CustomConfigurationInput"></a>

Input for custom configuration of a memory strategy.

## Contents
<a name="API_CustomConfigurationInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** episodicOverride **   <a name="bedrockagentcorecontrol-Type-CustomConfigurationInput-episodicOverride"></a>
The episodic memory strategy override configuration for a custom memory strategy.  
Type: [EpisodicOverrideConfigurationInput](API_EpisodicOverrideConfigurationInput.md) object  
Required: No

 ** selfManagedConfiguration **   <a name="bedrockagentcorecontrol-Type-CustomConfigurationInput-selfManagedConfiguration"></a>
The self managed configuration for a custom memory strategy.  
Type: [SelfManagedConfigurationInput](API_SelfManagedConfigurationInput.md) object  
Required: No

 ** semanticOverride **   <a name="bedrockagentcorecontrol-Type-CustomConfigurationInput-semanticOverride"></a>
The semantic override configuration for a custom memory strategy.  
Type: [SemanticOverrideConfigurationInput](API_SemanticOverrideConfigurationInput.md) object  
Required: No

 ** summaryOverride **   <a name="bedrockagentcorecontrol-Type-CustomConfigurationInput-summaryOverride"></a>
The summary override configuration for a custom memory strategy.  
Type: [SummaryOverrideConfigurationInput](API_SummaryOverrideConfigurationInput.md) object  
Required: No

 ** userPreferenceOverride **   <a name="bedrockagentcorecontrol-Type-CustomConfigurationInput-userPreferenceOverride"></a>
The user preference override configuration for a custom memory strategy.  
Type: [UserPreferenceOverrideConfigurationInput](API_UserPreferenceOverrideConfigurationInput.md) object  
Required: No

## See Also
<a name="API_CustomConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CustomConfigurationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CustomConfigurationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CustomConfigurationInput) 