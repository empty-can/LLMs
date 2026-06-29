

# AutomatedReasoningPolicyScenario
<a name="API_AutomatedReasoningPolicyScenario"></a>

Represents a test scenario used to validate an Automated Reasoning policy, including the test conditions and expected outcomes.

## Contents
<a name="API_AutomatedReasoningPolicyScenario_Contents"></a>

 ** alternateExpression **   <a name="bedrock-Type-AutomatedReasoningPolicyScenario-alternateExpression"></a>
An alternative way to express the same test scenario, used for validation and comparison purposes.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: Yes

 ** expectedResult **   <a name="bedrock-Type-AutomatedReasoningPolicyScenario-expectedResult"></a>
The expected outcome when this scenario is evaluated against the policy (e.g., PASS, FAIL, VIOLATION).  
Type: String  
Valid Values: `VALID | INVALID | SATISFIABLE | IMPOSSIBLE | TRANSLATION_AMBIGUOUS | TOO_COMPLEX | NO_TRANSLATION`   
Required: Yes

 ** expression **   <a name="bedrock-Type-AutomatedReasoningPolicyScenario-expression"></a>
The logical expression or condition that defines this test scenario.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: Yes

 ** ruleIds **   <a name="bedrock-Type-AutomatedReasoningPolicyScenario-ruleIds"></a>
The list of rule identifiers that are expected to be triggered or evaluated by this test scenario.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Fixed length of 12.  
Pattern: `[A-Z][0-9A-Z]{11}`   
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyScenario_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyScenario) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyScenario) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyScenario) 