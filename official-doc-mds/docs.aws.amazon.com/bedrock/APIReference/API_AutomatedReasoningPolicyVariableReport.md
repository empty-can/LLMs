

# AutomatedReasoningPolicyVariableReport
<a name="API_AutomatedReasoningPolicyVariableReport"></a>

Provides detailed fidelity analysis for a specific policy variable, including which source document statements support it and how accurate the variable definition is.

## Contents
<a name="API_AutomatedReasoningPolicyVariableReport_Contents"></a>

 ** policyVariable **   <a name="bedrock-Type-AutomatedReasoningPolicyVariableReport-policyVariable"></a>
The name of the policy variable being analyzed in this report.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[A-Za-z][A-Za-z0-9_]*`   
Required: Yes

 ** accuracyJustification **   <a name="bedrock-Type-AutomatedReasoningPolicyVariableReport-accuracyJustification"></a>
A textual explanation of the accuracy score, describing why the variable received this particular accuracy rating.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** accuracyScore **   <a name="bedrock-Type-AutomatedReasoningPolicyVariableReport-accuracyScore"></a>
A score from 0.0 to 1.0 indicating how accurately this variable represents concepts from the source material.  
Type: Double  
Valid Range: Minimum value of 0.0. Maximum value of 1.0.  
Required: No

 ** groundingJustifications **   <a name="bedrock-Type-AutomatedReasoningPolicyVariableReport-groundingJustifications"></a>
Explanations describing how the source statements support and justify this specific variable definition.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

 ** groundingStatements **   <a name="bedrock-Type-AutomatedReasoningPolicyVariableReport-groundingStatements"></a>
References to statements from the source documents that provide the basis or justification for this variable.  
Type: Array of [AutomatedReasoningPolicyStatementReference](API_AutomatedReasoningPolicyStatementReference.md) objects  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyVariableReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyVariableReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyVariableReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyVariableReport) 