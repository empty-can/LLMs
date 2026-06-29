

# AutomatedReasoningPolicyDefinitionRule
<a name="API_AutomatedReasoningPolicyDefinitionRule"></a>

Represents a formal logic rule in an Automated Reasoning policy. For example, rules can be expressed as if-then statements that define logical constraints.

## Contents
<a name="API_AutomatedReasoningPolicyDefinitionRule_Contents"></a>

 ** expression **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionRule-expression"></a>
The formal logic expression of the rule.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]+`   
Required: Yes

 ** id **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionRule-id"></a>
The unique identifier of the rule within the policy.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[A-Z][0-9A-Z]{11}`   
Required: Yes

 ** alternateExpression **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionRule-alternateExpression"></a>
The human-readable form of the rule expression, often in natural language or simplified notation.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `[\s\S]+`   
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyDefinitionRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionRule) 