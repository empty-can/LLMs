

# AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation
<a name="API_AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation"></a>

An annotation for updating the policy based on feedback about how specific rules performed during testing or real-world usage.

## Contents
<a name="API_AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation_Contents"></a>

 ** feedback **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation-feedback"></a>
The feedback information about rule performance, including suggestions for improvements or corrections.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: Yes

 ** ruleIds **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation-ruleIds"></a>
The list of rule identifiers that the feedback applies to.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Fixed length of 12.  
Pattern: `[A-Z][0-9A-Z]{11}`   
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation) 