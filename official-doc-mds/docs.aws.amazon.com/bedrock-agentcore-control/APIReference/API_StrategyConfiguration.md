

# StrategyConfiguration
<a name="API_StrategyConfiguration"></a>

Contains configuration information for a memory strategy.

## Contents
<a name="API_StrategyConfiguration_Contents"></a>

 ** consolidation **   <a name="bedrockagentcorecontrol-Type-StrategyConfiguration-consolidation"></a>
The consolidation configuration for the memory strategy.  
Type: [ConsolidationConfiguration](API_ConsolidationConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** extraction **   <a name="bedrockagentcorecontrol-Type-StrategyConfiguration-extraction"></a>
The extraction configuration for the memory strategy.  
Type: [ExtractionConfiguration](API_ExtractionConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** reflection **   <a name="bedrockagentcorecontrol-Type-StrategyConfiguration-reflection"></a>
The reflection configuration for the memory strategy.  
Type: [ReflectionConfiguration](API_ReflectionConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** selfManagedConfiguration **   <a name="bedrockagentcorecontrol-Type-StrategyConfiguration-selfManagedConfiguration"></a>
Self-managed configuration settings.  
Type: [SelfManagedConfiguration](API_SelfManagedConfiguration.md) object  
Required: No

 ** type **   <a name="bedrockagentcorecontrol-Type-StrategyConfiguration-type"></a>
The type of override for the strategy configuration.  
Type: String  
Valid Values: `SEMANTIC_OVERRIDE | SUMMARY_OVERRIDE | USER_PREFERENCE_OVERRIDE | SELF_MANAGED | EPISODIC_OVERRIDE`   
Required: No

## See Also
<a name="API_StrategyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/StrategyConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/StrategyConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/StrategyConfiguration) 