

# GuardrailAutomatedReasoningInvalidFinding
<a name="API_runtime_GuardrailAutomatedReasoningInvalidFinding"></a>

Indicates that the claims are logically false and contradictory to the established rules or premises.

## Contents
<a name="API_runtime_GuardrailAutomatedReasoningInvalidFinding_Contents"></a>

 ** contradictingRules **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningInvalidFinding-contradictingRules"></a>
The automated reasoning policy rules that contradict the claims in the input.  
Type: Array of [GuardrailAutomatedReasoningRule](API_runtime_GuardrailAutomatedReasoningRule.md) objects  
Required: No

 ** logicWarning **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningInvalidFinding-logicWarning"></a>
Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.  
Type: [GuardrailAutomatedReasoningLogicWarning](API_runtime_GuardrailAutomatedReasoningLogicWarning.md) object  
Required: No

 ** translation **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningInvalidFinding-translation"></a>
The logical translation of the input that this finding invalidates.  
Type: [GuardrailAutomatedReasoningTranslation](API_runtime_GuardrailAutomatedReasoningTranslation.md) object  
Required: No

## See Also
<a name="API_runtime_GuardrailAutomatedReasoningInvalidFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningInvalidFinding) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningInvalidFinding) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningInvalidFinding) 