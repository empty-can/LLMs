

# GuardrailAutomatedReasoningLogicWarning
<a name="API_runtime_GuardrailAutomatedReasoningLogicWarning"></a>

Identifies logical issues in the translated statements that exist independent of any policy rules, such as statements that are always true or always false.

## Contents
<a name="API_runtime_GuardrailAutomatedReasoningLogicWarning_Contents"></a>

 ** claims **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningLogicWarning-claims"></a>
The logical statements that are validated while assuming the policy and premises.  
Type: Array of [GuardrailAutomatedReasoningStatement](API_runtime_GuardrailAutomatedReasoningStatement.md) objects  
Required: No

 ** premises **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningLogicWarning-premises"></a>
The logical statements that serve as premises under which the claims are validated.  
Type: Array of [GuardrailAutomatedReasoningStatement](API_runtime_GuardrailAutomatedReasoningStatement.md) objects  
Required: No

 ** type **   <a name="bedrock-Type-runtime_GuardrailAutomatedReasoningLogicWarning-type"></a>
The category of the detected logical issue, such as statements that are always true or always false.  
Type: String  
Valid Values: `ALWAYS_FALSE | ALWAYS_TRUE`   
Required: No

## See Also
<a name="API_runtime_GuardrailAutomatedReasoningLogicWarning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningLogicWarning) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningLogicWarning) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailAutomatedReasoningLogicWarning) 