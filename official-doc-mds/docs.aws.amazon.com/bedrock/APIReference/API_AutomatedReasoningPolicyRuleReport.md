

# AutomatedReasoningPolicyRuleReport
<a name="API_AutomatedReasoningPolicyRuleReport"></a>

Provides detailed fidelity analysis for a specific policy rule, including which source document statements support it and how accurate the rule is.

## Contents
<a name="API_AutomatedReasoningPolicyRuleReport_Contents"></a>

 ** rule **   <a name="bedrock-Type-AutomatedReasoningPolicyRuleReport-rule"></a>
The identifier of the policy rule being analyzed in this report.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[A-Z][0-9A-Z]{11}`   
Required: Yes

 ** accuracyJustification **   <a name="bedrock-Type-AutomatedReasoningPolicyRuleReport-accuracyJustification"></a>
A textual explanation of the accuracy score, describing why the rule received this particular accuracy rating.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** accuracyScore **   <a name="bedrock-Type-AutomatedReasoningPolicyRuleReport-accuracyScore"></a>
A score from 0.0 to 1.0 indicating how accurately this rule represents the source material.  
Type: Double  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: No

 ** groundingJustifications **   <a name="bedrock-Type-AutomatedReasoningPolicyRuleReport-groundingJustifications"></a>
Explanations describing how the source statements support and justify this specific rule.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** groundingStatements **   <a name="bedrock-Type-AutomatedReasoningPolicyRuleReport-groundingStatements"></a>
References to statements from the source documents that provide the basis or justification for this rule.  
Type: Array of [AutomatedReasoningPolicyStatementReference](API_AutomatedReasoningPolicyStatementReference.md) objects  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyRuleReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyRuleReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyRuleReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyRuleReport) 