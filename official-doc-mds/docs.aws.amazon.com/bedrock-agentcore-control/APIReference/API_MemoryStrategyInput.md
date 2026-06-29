

# MemoryStrategyInput
<a name="API_MemoryStrategyInput"></a>

Contains input information for creating a memory strategy.

## Contents
<a name="API_MemoryStrategyInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customMemoryStrategy **   <a name="bedrockagentcorecontrol-Type-MemoryStrategyInput-customMemoryStrategy"></a>
Input for creating a custom memory strategy.  
Type: [CustomMemoryStrategyInput](API_CustomMemoryStrategyInput.md) object  
Required: No

 ** episodicMemoryStrategy **   <a name="bedrockagentcorecontrol-Type-MemoryStrategyInput-episodicMemoryStrategy"></a>
Input for creating an episodic memory strategy  
Type: [EpisodicMemoryStrategyInput](API_EpisodicMemoryStrategyInput.md) object  
Required: No

 ** semanticMemoryStrategy **   <a name="bedrockagentcorecontrol-Type-MemoryStrategyInput-semanticMemoryStrategy"></a>
Input for creating a semantic memory strategy.  
Type: [SemanticMemoryStrategyInput](API_SemanticMemoryStrategyInput.md) object  
Required: No

 ** summaryMemoryStrategy **   <a name="bedrockagentcorecontrol-Type-MemoryStrategyInput-summaryMemoryStrategy"></a>
Input for creating a summary memory strategy.  
Type: [SummaryMemoryStrategyInput](API_SummaryMemoryStrategyInput.md) object  
Required: No

 ** userPreferenceMemoryStrategy **   <a name="bedrockagentcorecontrol-Type-MemoryStrategyInput-userPreferenceMemoryStrategy"></a>
Input for creating a user preference memory strategy.  
Type: [UserPreferenceMemoryStrategyInput](API_UserPreferenceMemoryStrategyInput.md) object  
Required: No

## See Also
<a name="API_MemoryStrategyInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/MemoryStrategyInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/MemoryStrategyInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/MemoryStrategyInput) 