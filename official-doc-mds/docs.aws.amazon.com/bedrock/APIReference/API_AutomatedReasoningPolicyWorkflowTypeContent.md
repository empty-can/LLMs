

# AutomatedReasoningPolicyWorkflowTypeContent
<a name="API_AutomatedReasoningPolicyWorkflowTypeContent"></a>

Defines the content and configuration for different types of policy build workflows.

## Contents
<a name="API_AutomatedReasoningPolicyWorkflowTypeContent_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** documents **   <a name="bedrock-Type-AutomatedReasoningPolicyWorkflowTypeContent-documents"></a>
The list of documents to be processed in a document ingestion workflow.  
Type: Array of [AutomatedReasoningPolicyBuildWorkflowDocument](API_AutomatedReasoningPolicyBuildWorkflowDocument.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

 ** generateFidelityReportContent **   <a name="bedrock-Type-AutomatedReasoningPolicyWorkflowTypeContent-generateFidelityReportContent"></a>
The content configuration for generating a fidelity report workflow. This can include source documents to analyze or an existing fidelity report to update with a new policy definition.  
Type: [AutomatedReasoningPolicyGenerateFidelityReportContent](API_AutomatedReasoningPolicyGenerateFidelityReportContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** iterativeRefinementContent **   <a name="bedrock-Type-AutomatedReasoningPolicyWorkflowTypeContent-iterativeRefinementContent"></a>
Content configuration to start an iterative policy refinement workflow that uses generative AI to automatically make changes to the policy based on test results and the optional feedback provided.  
Type: [AutomatedReasoningPolicyIterativeRefinementContent](API_AutomatedReasoningPolicyIterativeRefinementContent.md) object  
Required: No

 ** policyRepairAssets **   <a name="bedrock-Type-AutomatedReasoningPolicyWorkflowTypeContent-policyRepairAssets"></a>
The assets and instructions needed for a policy repair workflow, including repair annotations and guidance.  
Type: [AutomatedReasoningPolicyBuildWorkflowRepairContent](API_AutomatedReasoningPolicyBuildWorkflowRepairContent.md) object  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyWorkflowTypeContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyWorkflowTypeContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyWorkflowTypeContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyWorkflowTypeContent) 