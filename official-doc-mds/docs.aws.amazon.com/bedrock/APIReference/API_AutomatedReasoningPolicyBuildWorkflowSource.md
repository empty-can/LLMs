

# AutomatedReasoningPolicyBuildWorkflowSource
<a name="API_AutomatedReasoningPolicyBuildWorkflowSource"></a>

Defines the source content for a policy build workflow, which can include documents, repair instructions, or other input materials.

## Contents
<a name="API_AutomatedReasoningPolicyBuildWorkflowSource_Contents"></a>

 ** policyDefinition **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowSource-policyDefinition"></a>
An existing policy definition that serves as the starting point for the build workflow, typically used in policy repair or update scenarios.  
Type: [AutomatedReasoningPolicyDefinition](API_AutomatedReasoningPolicyDefinition.md) object  
Required: No

 ** workflowContent **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowSource-workflowContent"></a>
The actual content to be processed in the build workflow, such as documents to analyze or repair instructions to apply.  
Type: [AutomatedReasoningPolicyWorkflowTypeContent](API_AutomatedReasoningPolicyWorkflowTypeContent.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_AutomatedReasoningPolicyBuildWorkflowSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyBuildWorkflowSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyBuildWorkflowSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyBuildWorkflowSource) 