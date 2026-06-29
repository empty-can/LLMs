

# GuardrailAutomatedReasoningImpossibleFinding
<a name="API_runtime_GuardrailAutomatedReasoningImpossibleFinding"></a>

Indicates that no valid claims can be made due to logical contradictions in the premises or rules.

## Contents
<a name="API_runtime_GuardrailAutomatedReasoningImpossibleFinding_Contents"></a>

 ** contradictingRules **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningImpossibleFinding-contradictingRules"></a>
The automated reasoning policy rules that contradict the claims and/or premises in the input.  
Type: Array of [GuardrailAutomatedReasoningRule](API_runtime_GuardrailAutomatedReasoningRule.md) objects  
Required: No

 ** logicWarning **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningImpossibleFinding-logicWarning"></a>
Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.  
Type: [GuardrailAutomatedReasoningLogicWarning](API_runtime_GuardrailAutomatedReasoningLogicWarning.md) object  
Required: No

 ** translation **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningImpossibleFinding-translation"></a>
The logical translation of the input that this finding evaluates.  
Type: [GuardrailAutomatedReasoningTranslation](API_runtime_GuardrailAutomatedReasoningTranslation.md) object  
Required: No

## See Also
<a name="API_runtime_GuardrailAutomatedReasoningImpossibleFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningImpossibleFinding) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningImpossibleFinding) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningImpossibleFinding) 