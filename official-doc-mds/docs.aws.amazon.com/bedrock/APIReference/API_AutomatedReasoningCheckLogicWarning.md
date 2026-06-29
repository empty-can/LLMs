

# AutomatedReasoningCheckLogicWarning
<a name="API_AutomatedReasoningCheckLogicWarning"></a>

Identifies logical issues in the translated statements that exist independent of any policy rules, such as statements that are always true or always false.

## Contents
<a name="API_AutomatedReasoningCheckLogicWarning_Contents"></a>

 ** claims **   <a name="bedrock-Type-AutomatedReasoningCheckLogicWarning-claims"></a>
The logical statements that are validated while assuming the policy and premises.  
Type: Array of [AutomatedReasoningLogicStatement](API_AutomatedReasoningLogicStatement.md) objects  
Required: No

 ** premises **   <a name="bedrock-Type-AutomatedReasoningCheckLogicWarning-premises"></a>
The logical statements that serve as premises under which the claims are validated.  
Type: Array of [AutomatedReasoningLogicStatement](API_AutomatedReasoningLogicStatement.md) objects  
Required: No

 ** type **   <a name="bedrock-Type-AutomatedReasoningCheckLogicWarning-type"></a>
The category of the detected logical issue, such as statements that are always true or always false.  
Type: String  
Valid Values: `ALWAYS_TRUE | ALWAYS_FALSE`   
Required: No

## See Also
<a name="API_AutomatedReasoningCheckLogicWarning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningCheckLogicWarning) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningCheckLogicWarning) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningCheckLogicWarning) 