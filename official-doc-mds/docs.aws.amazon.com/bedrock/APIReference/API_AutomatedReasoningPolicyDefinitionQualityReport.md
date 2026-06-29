

# AutomatedReasoningPolicyDefinitionQualityReport
<a name="API_AutomatedReasoningPolicyDefinitionQualityReport"></a>

Provides a comprehensive analysis of the quality and completeness of an Automated Reasoning policy definition, highlighting potential issues and optimization opportunities.

## Contents
<a name="API_AutomatedReasoningPolicyDefinitionQualityReport_Contents"></a>

 ** conflictingRules **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionQualityReport-conflictingRules"></a>
A list of rules that may conflict with each other, potentially leading to inconsistent policy behavior.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 500 items.  
Length Constraints: Fixed length of 12.  
Pattern: `[A-Z][0-9A-Z]{11}`   
Required: Yes

 ** disjointRuleSets **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionQualityReport-disjointRuleSets"></a>
Groups of rules that operate on completely separate sets of variables, indicating the policy may be addressing multiple unrelated concerns.  
Type: Array of [AutomatedReasoningPolicyDisjointRuleSet](API_AutomatedReasoningPolicyDisjointRuleSet.md) objects  
Required: Yes

 ** ruleCount **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionQualityReport-ruleCount"></a>
The total number of rules defined in the policy.  
Type: Integer  
Required: Yes

 ** typeCount **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionQualityReport-typeCount"></a>
The total number of custom types defined in the policy.  
Type: Integer  
Required: Yes

 ** unusedTypes **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionQualityReport-unusedTypes"></a>
A list of custom types that are defined but not referenced by any variables or rules, suggesting they may be unnecessary.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 150 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** unusedTypeValues **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionQualityReport-unusedTypeValues"></a>
A list of type values that are defined but never used in any rules, indicating potential cleanup opportunities.  
Type: Array of [AutomatedReasoningPolicyDefinitionTypeValuePair](API_AutomatedReasoningPolicyDefinitionTypeValuePair.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 22500 items.  
Required: Yes

 ** unusedVariables **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionQualityReport-unusedVariables"></a>
A list of variables that are defined but not referenced by any rules, suggesting they may be unnecessary.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 600 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** variableCount **   <a name="bedrock-Type-AutomatedReasoningPolicyDefinitionQualityReport-variableCount"></a>
The total number of variables defined in the policy.  
Type: Integer  
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyDefinitionQualityReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionQualityReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionQualityReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyDefinitionQualityReport) 