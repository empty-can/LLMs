

# AutomatedReasoningPolicyFidelityReport
<a name="API_AutomatedReasoningPolicyFidelityReport"></a>

A comprehensive analysis report that measures how accurately a generated policy represents the source documents. The report includes coverage and accuracy scores, detailed grounding information linking policy elements to source statements, and annotated document content.

## Contents
<a name="API_AutomatedReasoningPolicyFidelityReport_Contents"></a>

 ** accuracyScore **   <a name="bedrock-Type-AutomatedReasoningPolicyFidelityReport-accuracyScore"></a>
A score from 0.0 to 1.0 indicating how accurate the policy rules are relative to the source documents. A higher score means the policy rules more faithfully represent the source material.  
Type: Double  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: Yes

 ** coverageScore **   <a name="bedrock-Type-AutomatedReasoningPolicyFidelityReport-coverageScore"></a>
A score from 0.0 to 1.0 indicating how well the policy covers the statements in the source documents. A higher score means more of the source content is represented in the policy.  
Type: Double  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: Yes

 ** documentSources **   <a name="bedrock-Type-AutomatedReasoningPolicyFidelityReport-documentSources"></a>
A list of source documents with their content broken down into atomic statements and annotated with line numbers for precise referencing.  
Type: Array of [AutomatedReasoningPolicyReportSourceDocument](API_AutomatedReasoningPolicyReportSourceDocument.md) objects  
Required: Yes

 ** ruleReports **   <a name="bedrock-Type-AutomatedReasoningPolicyFidelityReport-ruleReports"></a>
A mapping from rule identifiers to detailed fidelity reports for each rule, showing which source statements ground each rule and how accurate it is.  
Type: String to [AutomatedReasoningPolicyRuleReport](API_AutomatedReasoningPolicyRuleReport.md) object map  
Key Length Constraints: Fixed length of 12.  
Key Pattern: `[A-Z][0-9A-Z]{11}`   
Required: Yes

 ** variableReports **   <a name="bedrock-Type-AutomatedReasoningPolicyFidelityReport-variableReports"></a>
A mapping from variable names to detailed fidelity reports for each variable, showing which source statements ground each variable and how accurate it is.  
Type: String to [AutomatedReasoningPolicyVariableReport](API_AutomatedReasoningPolicyVariableReport.md) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 64.  
Key Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyFidelityReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyFidelityReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyFidelityReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyFidelityReport) 