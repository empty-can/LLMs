

# AutomatedReasoningPolicyGenerateFidelityReportContent
<a name="API_AutomatedReasoningPolicyGenerateFidelityReportContent"></a>

Configuration for generating a fidelity report, which can either analyze new documents or update an existing fidelity report with a new policy definition.

## Contents
<a name="API_AutomatedReasoningPolicyGenerateFidelityReportContent_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** documents **   <a name="bedrock-Type-AutomatedReasoningPolicyGenerateFidelityReportContent-documents"></a>
Source documents to analyze for generating a new fidelity report. The documents will be processed to create atomic statements and grounding information.  
Type: Array of [AutomatedReasoningPolicyBuildWorkflowDocument](API_AutomatedReasoningPolicyBuildWorkflowDocument.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyGenerateFidelityReportContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyGenerateFidelityReportContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyGenerateFidelityReportContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyGenerateFidelityReportContent) 