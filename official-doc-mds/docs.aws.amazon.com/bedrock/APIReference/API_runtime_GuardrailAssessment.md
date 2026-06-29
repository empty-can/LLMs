

# GuardrailAssessment
<a name="API_runtime_GuardrailAssessment"></a>

A behavior assessment of the guardrail policies used in a call to the Converse API. 

## Contents
<a name="API_runtime_GuardrailAssessment_Contents"></a>

 ** appliedGuardrailDetails **   <a name="bedrock-Type-runtime_GuardrailAssessment-appliedGuardrailDetails"></a>
Details about the specific guardrail that was applied during this assessment, including its identifier, version, ARN, origin, and ownership information.  
Type: [AppliedGuardrailDetails](API_runtime_AppliedGuardrailDetails.md) object  
Required: No

 ** automatedReasoningPolicy **   <a name="bedrock-Type-runtime_GuardrailAssessment-automatedReasoningPolicy"></a>
The automated reasoning policy assessment results, including logical validation findings for the input content.  
Type: [GuardrailAutomatedReasoningPolicyAssessment](API_runtime_GuardrailAutomatedReasoningPolicyAssessment.md) object  
Required: No

 ** contentPolicy **   <a name="bedrock-Type-runtime_GuardrailAssessment-contentPolicy"></a>
The content policy.  
Type: [GuardrailContentPolicyAssessment](API_runtime_GuardrailContentPolicyAssessment.md) object  
Required: No

 ** contextualGroundingPolicy **   <a name="bedrock-Type-runtime_GuardrailAssessment-contextualGroundingPolicy"></a>
The contextual grounding policy used for the guardrail assessment.  
Type: [GuardrailContextualGroundingPolicyAssessment](API_runtime_GuardrailContextualGroundingPolicyAssessment.md) object  
Required: No

 ** invocationMetrics **   <a name="bedrock-Type-runtime_GuardrailAssessment-invocationMetrics"></a>
The invocation metrics for the guardrail assessment.  
Type: [GuardrailInvocationMetrics](API_runtime_GuardrailInvocationMetrics.md) object  
Required: No

 ** sensitiveInformationPolicy **   <a name="bedrock-Type-runtime_GuardrailAssessment-sensitiveInformationPolicy"></a>
The sensitive information policy.  
Type: [GuardrailSensitiveInformationPolicyAssessment](API_runtime_GuardrailSensitiveInformationPolicyAssessment.md) object  
Required: No

 ** topicPolicy **   <a name="bedrock-Type-runtime_GuardrailAssessment-topicPolicy"></a>
The topic policy.  
Type: [GuardrailTopicPolicyAssessment](API_runtime_GuardrailTopicPolicyAssessment.md) object  
Required: No

 ** wordPolicy **   <a name="bedrock-Type-runtime_GuardrailAssessment-wordPolicy"></a>
The word policy.  
Type: [GuardrailWordPolicyAssessment](API_runtime_GuardrailWordPolicyAssessment.md) object  
Required: No

## See Also
<a name="API_runtime_GuardrailAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailAssessment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailAssessment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailAssessment) 