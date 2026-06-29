

# GuardrailAutomatedReasoningTranslationAmbiguousFinding
<a name="API_runtime_GuardrailAutomatedReasoningTranslationAmbiguousFinding"></a>

Indicates that the input has multiple valid logical interpretations, requiring additional context or clarification.

## Contents
<a name="API_runtime_GuardrailAutomatedReasoningTranslationAmbiguousFinding_Contents"></a>

 ** differenceScenarios **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningTranslationAmbiguousFinding-differenceScenarios"></a>
Scenarios showing how the different translation options differ in meaning.  
Type: Array of [GuardrailAutomatedReasoningScenario](API_runtime_GuardrailAutomatedReasoningScenario.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 2 items.  
Required: No

 ** options **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningTranslationAmbiguousFinding-options"></a>
Different logical interpretations that were detected during translation of the input.  
Type: Array of [GuardrailAutomatedReasoningTranslationOption](API_runtime_GuardrailAutomatedReasoningTranslationOption.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 2 items.  
Required: No

## See Also
<a name="API_runtime_GuardrailAutomatedReasoningTranslationAmbiguousFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningTranslationAmbiguousFinding) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningTranslationAmbiguousFinding) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningTranslationAmbiguousFinding) 