

# GuardrailAutomatedReasoningFinding
<a name="API_runtime_GuardrailAutomatedReasoningFinding"></a>

Represents a logical validation result from automated reasoning policy evaluation. The finding indicates whether claims in the input are logically valid, invalid, satisfiable, impossible, or have other logical issues.

## Contents
<a name="API_runtime_GuardrailAutomatedReasoningFinding_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** impossible **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningFinding-impossible"></a>
Contains the result when the automated reasoning evaluation determines that no valid logical conclusions can be drawn due to contradictions in the premises or policy rules themselves.  
Type: [GuardrailAutomatedReasoningImpossibleFinding](API_runtime_GuardrailAutomatedReasoningImpossibleFinding.md) object  
Required: No

 ** invalid **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningFinding-invalid"></a>
Contains the result when the automated reasoning evaluation determines that the claims in the input are logically invalid and contradict the established premises or policy rules.  
Type: [GuardrailAutomatedReasoningInvalidFinding](API_runtime_GuardrailAutomatedReasoningInvalidFinding.md) object  
Required: No

 ** noTranslations **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningFinding-noTranslations"></a>
Contains the result when the automated reasoning evaluation cannot extract any relevant logical information from the input that can be validated against the policy rules.  
Type: [GuardrailAutomatedReasoningNoTranslationsFinding](API_runtime_GuardrailAutomatedReasoningNoTranslationsFinding.md) object  
Required: No

 ** satisfiable **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningFinding-satisfiable"></a>
Contains the result when the automated reasoning evaluation determines that the claims in the input could be either true or false depending on additional assumptions not provided in the input context.  
Type: [GuardrailAutomatedReasoningSatisfiableFinding](API_runtime_GuardrailAutomatedReasoningSatisfiableFinding.md) object  
Required: No

 ** tooComplex **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningFinding-tooComplex"></a>
Contains the result when the automated reasoning evaluation cannot process the input due to its complexity or volume exceeding the system's processing capacity for logical analysis.  
Type: [GuardrailAutomatedReasoningTooComplexFinding](API_runtime_GuardrailAutomatedReasoningTooComplexFinding.md) object  
Required: No

 ** translationAmbiguous **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningFinding-translationAmbiguous"></a>
Contains the result when the automated reasoning evaluation detects that the input has multiple valid logical interpretations, requiring additional context or clarification to proceed with validation.  
Type: [GuardrailAutomatedReasoningTranslationAmbiguousFinding](API_runtime_GuardrailAutomatedReasoningTranslationAmbiguousFinding.md) object  
Required: No

 ** valid **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningFinding-valid"></a>
Contains the result when the automated reasoning evaluation determines that the claims in the input are logically valid and definitively true based on the provided premises and policy rules.  
Type: [GuardrailAutomatedReasoningValidFinding](API_runtime_GuardrailAutomatedReasoningValidFinding.md) object  
Required: No

## See Also
<a name="API_runtime_GuardrailAutomatedReasoningFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningFinding) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningFinding) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningFinding) 