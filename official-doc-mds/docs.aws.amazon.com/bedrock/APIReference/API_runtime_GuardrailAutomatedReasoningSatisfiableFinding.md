

# GuardrailAutomatedReasoningSatisfiableFinding
<a name="API_runtime_GuardrailAutomatedReasoningSatisfiableFinding"></a>

Indicates that the claims could be either true or false depending on additional assumptions not provided in the input.

## Contents
<a name="API_runtime_GuardrailAutomatedReasoningSatisfiableFinding_Contents"></a>

 ** claimsFalseScenario **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningSatisfiableFinding-claimsFalseScenario"></a>
An example scenario demonstrating how the claims could be logically false.  
Type: [GuardrailAutomatedReasoningScenario](API_runtime_GuardrailAutomatedReasoningScenario.md) object  
Required: No

 ** claimsTrueScenario **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningSatisfiableFinding-claimsTrueScenario"></a>
An example scenario demonstrating how the claims could be logically true.  
Type: [GuardrailAutomatedReasoningScenario](API_runtime_GuardrailAutomatedReasoningScenario.md) object  
Required: No

 ** logicWarning **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningSatisfiableFinding-logicWarning"></a>
Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.  
Type: [GuardrailAutomatedReasoningLogicWarning](API_runtime_GuardrailAutomatedReasoningLogicWarning.md) object  
Required: No

 ** translation **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningSatisfiableFinding-translation"></a>
The logical translation of the input that this finding evaluates.  
Type: [GuardrailAutomatedReasoningTranslation](API_runtime_GuardrailAutomatedReasoningTranslation.md) object  
Required: No

## See Also
<a name="API_runtime_GuardrailAutomatedReasoningSatisfiableFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningSatisfiableFinding) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningSatisfiableFinding) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningSatisfiableFinding) 