

# AutomatedReasoningPolicyBuildWorkflowSummary
<a name="API_AutomatedReasoningPolicyBuildWorkflowSummary"></a>

Provides a summary of a policy build workflow, including its current status, timing information, and key identifiers.

## Contents
<a name="API_AutomatedReasoningPolicyBuildWorkflowSummary_Contents"></a>

 ** buildWorkflowId **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowSummary-buildWorkflowId"></a>
The unique identifier of the build workflow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}`   
Required: Yes

 ** buildWorkflowType **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowSummary-buildWorkflowType"></a>
The type of build workflow (e.g., DOCUMENT\_INGESTION, POLICY\_REPAIR).  
Type: String  
Valid Values: `INGEST_CONTENT | REFINE_POLICY | IMPORT_POLICY | GENERATE_FIDELITY_REPORT | GENERATE_POLICY_SCENARIOS | RESOLVE_POLICY_AMBIGUITIES | ITERATIVELY_REFINE_POLICY`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowSummary-createdAt"></a>
The timestamp when the build workflow was created.  
Type: Timestamp  
Required: Yes

 ** policyArn **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowSummary-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy associated with this build workflow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

 ** status **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowSummary-status"></a>
The current status of the build workflow (e.g., RUNNING, COMPLETED, FAILED, CANCELLED).  
Type: String  
Valid Values: `SCHEDULED | CANCEL_REQUESTED | PREPROCESSING | BUILDING | TESTING | COMPLETED | FAILED | CANCELLED`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-AutomatedReasoningPolicyBuildWorkflowSummary-updatedAt"></a>
The timestamp when the build workflow was last updated.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_AutomatedReasoningPolicyBuildWorkflowSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/AutomatedReasoningPolicyBuildWorkflowSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/AutomatedReasoningPolicyBuildWorkflowSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/AutomatedReasoningPolicyBuildWorkflowSummary) 