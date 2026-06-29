

# GuardrailAutomatedReasoningValidFinding
<a name="API_runtime_GuardrailAutomatedReasoningValidFinding"></a>

Indicates that the claims are definitively true and logically implied by the premises, with no possible alternative interpretations.

## Contents
<a name="API_runtime_GuardrailAutomatedReasoningValidFinding_Contents"></a>

 ** claimsTrueScenario **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningValidFinding-claimsTrueScenario"></a>
An example scenario demonstrating how the claims are logically true.  
Type: [GuardrailAutomatedReasoningScenario](API_runtime_GuardrailAutomatedReasoningScenario.md) object  
Required: No

 ** logicWarning **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningValidFinding-logicWarning"></a>
Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.  
Type: [GuardrailAutomatedReasoningLogicWarning](API_runtime_GuardrailAutomatedReasoningLogicWarning.md) object  
Required: No

 ** supportingRules **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningValidFinding-supportingRules"></a>
The automated reasoning policy rules that support why this result is considered valid.  
Type: Array of [GuardrailAutomatedReasoningRule](API_runtime_GuardrailAutomatedReasoningRule.md) objects  
Required: No

 ** translation **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningValidFinding-translation"></a>
The logical translation of the input that this finding validates.  
Type: [GuardrailAutomatedReasoningTranslation](API_runtime_GuardrailAutomatedReasoningTranslation.md) object  
Required: No

## See Also
<a name="API_runtime_GuardrailAutomatedReasoningValidFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningValidFinding) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningValidFinding) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningValidFinding) 