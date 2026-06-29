

# AutomatedReasoningPolicyUpdateRuleAnnotation
<a name="API_AutomatedReasoningPolicyUpdateRuleAnnotation"></a>

An annotation for modifying an existing rule in an Automated Reasoning policy.

## Contents
<a name="API_AutomatedReasoningPolicyUpdateRuleAnnotation_Contents"></a>

 ** expression **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateRuleAnnotation-expression"></a>
The new formal logical expression for the rule, replacing the previous expression.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]+`   
Required: Yes

 ** ruleId **   <a name="bedrock-Type-AutomatedReasoningPolicyUpdateRuleAnnotation-ruleId"></a>
The unique identifier of the rule to update.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[A-Z][0-9A-Z]{11}`   
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyUpdateRuleAnnotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateRuleAnnotation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateRuleAnnotation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyUpdateRuleAnnotation) 