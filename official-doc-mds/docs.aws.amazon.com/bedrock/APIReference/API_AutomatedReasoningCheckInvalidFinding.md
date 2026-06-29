

# AutomatedReasoningCheckInvalidFinding
<a name="API_AutomatedReasoningCheckInvalidFinding"></a>

Indicates that the claims are logically false and contradictory to the established rules or premises.

## Contents
<a name="API_AutomatedReasoningCheckInvalidFinding_Contents"></a>

 ** contradictingRules **   <a name="bedrock-Type-AutomatedReasoningCheckInvalidFinding-contradictingRules"></a>
The automated reasoning policy rules that contradict the claims in the input.  
Type: Array of [AutomatedReasoningCheckRule](API_AutomatedReasoningCheckRule.md) objects  
Required: No

 ** logicWarning **   <a name="bedrock-Type-AutomatedReasoningCheckInvalidFinding-logicWarning"></a>
Indication of a logic issue with the translation without needing to consider the automated reasoning policy rules.  
Type: [AutomatedReasoningCheckLogicWarning](API_AutomatedReasoningCheckLogicWarning.md) object  
Required: No

 ** translation **   <a name="bedrock-Type-AutomatedReasoningCheckInvalidFinding-translation"></a>
The logical translation of the input that this finding invalidates.  
Type: [AutomatedReasoningCheckTranslation](API_AutomatedReasoningCheckTranslation.md) object  
Required: No

## See Also
<a name="API_AutomatedReasoningCheckInvalidFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningCheckInvalidFinding) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningCheckInvalidFinding) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningCheckInvalidFinding) 