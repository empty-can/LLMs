

# GuardrailAutomatedReasoningTranslation
<a name="API_runtime_GuardrailAutomatedReasoningTranslation"></a>

Contains the logical translation of natural language input into formal logical statements, including premises, claims, and confidence scores.

## Contents
<a name="API_runtime_GuardrailAutomatedReasoningTranslation_Contents"></a>

 ** claims **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningTranslation-claims"></a>
The logical statements that are being validated against the premises and policy rules.  
Type: Array of [GuardrailAutomatedReasoningStatement](API_runtime_GuardrailAutomatedReasoningStatement.md) objects  
Required: No

 ** confidence **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningTranslation-confidence"></a>
A confidence score between 0 and 1 indicating how certain the system is about the logical translation.  
Type: Double  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

 ** premises **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningTranslation-premises"></a>
The logical statements that serve as the foundation or assumptions for the claims.  
Type: Array of [GuardrailAutomatedReasoningStatement](API_runtime_GuardrailAutomatedReasoningStatement.md) objects  
Required: No

 ** untranslatedClaims **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningTranslation-untranslatedClaims"></a>
References to portions of the original input text that correspond to the claims but could not be fully translated.  
Type: Array of [GuardrailAutomatedReasoningInputTextReference](API_runtime_GuardrailAutomatedReasoningInputTextReference.md) objects  
Required: No

 ** untranslatedPremises **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningTranslation-untranslatedPremises"></a>
References to portions of the original input text that correspond to the premises but could not be fully translated.  
Type: Array of [GuardrailAutomatedReasoningInputTextReference](API_runtime_GuardrailAutomatedReasoningInputTextReference.md) objects  
Required: No

## See Also
<a name="API_runtime_GuardrailAutomatedReasoningTranslation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningTranslation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningTranslation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningTranslation) 