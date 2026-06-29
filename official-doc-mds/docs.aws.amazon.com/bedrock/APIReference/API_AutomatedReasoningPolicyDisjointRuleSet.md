

# AutomatedReasoningPolicyDisjointRuleSet
<a name="API_AutomatedReasoningPolicyDisjointRuleSet"></a>

Represents a set of rules that operate on completely separate variables, indicating they address different concerns or domains within the policy.

## Contents
<a name="API_AutomatedReasoningPolicyDisjointRuleSet_Contents"></a>

 ** rules **   <a name="bedrock-Type-AutomatedReasoningPolicyDisjointRuleSet-rules"></a>
The list of rules that form this disjoint set, all operating on the same set of variables.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 500 items.  
Length Constraints: Fixed length of 12.  
Pattern: `[A-Z][0-9A-Z]{11}`   
Required: Yes

 ** variables **   <a name="bedrock-Type-AutomatedReasoningPolicyDisjointRuleSet-variables"></a>
The set of variables that are used by the rules in this disjoint set.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 600 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyDisjointRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyDisjointRuleSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyDisjointRuleSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyDisjointRuleSet) 