

# AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation
<a name="API_AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation"></a>

An annotation for updating the policy based on feedback about how it performed on specific test scenarios.

## Contents
<a name="API_AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation_Contents"></a>

 ** scenarioExpression **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation-scenarioExpression"></a>
The logical expression that defines the test scenario that generated this feedback.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: Yes

 ** feedback **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation-feedback"></a>
The feedback information about scenario performance, including any issues or improvements identified.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[\s\S]+`   
Required: No

 ** ruleIds **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation-ruleIds"></a>
The list of rule identifiers that were involved in the scenario being evaluated.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Fixed length of 12.  
Pattern: `[A-Z][0-9A-Z]{11}`   
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation) 