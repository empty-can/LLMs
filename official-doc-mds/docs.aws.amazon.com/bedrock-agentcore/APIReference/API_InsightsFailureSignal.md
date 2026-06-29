

# InsightsFailureSignal
<a name="API_InsightsFailureSignal"></a>

A signal indicating a detected failure within a span.

## Contents
<a name="API_InsightsFailureSignal_Contents"></a>

 ** category **   <a name="BedrockAgentCore-Type-InsightsFailureSignal-category"></a>
The failure category classification for this signal.  
Type: String  
Valid Values: `execution-error-category-authentication | execution-error-category-resource-not-found | execution-error-category-service-errors | execution-error-category-rate-limiting | execution-error-category-formatting | execution-error-category-timeout | execution-error-category-resource-exhaustion | execution-error-category-environment | execution-error-category-tool-schema | task-instruction-category-non-compliance | task-instruction-category-problem-id | incorrect-actions-category-tool-selection | incorrect-actions-category-poor-information-retrieval | incorrect-actions-category-clarification | incorrect-actions-category-inappropriate-info-request | context-handling-error-category-context-handling-failures | hallucination-category-hall-capabilities | hallucination-category-hall-misunderstand | hallucination-category-hall-usage | hallucination-category-hall-history | hallucination-category-hall-params | hallucination-category-fabricate-tool-outputs | repetitive-behavior-category-repetition-tool | repetitive-behavior-category-repetition-info | repetitive-behavior-category-step-repetition | orchestration-related-errors-category-reasoning-mismatch | orchestration-related-errors-category-goal-deviation | orchestration-related-errors-category-premature-termination | orchestration-related-errors-category-unaware-termination | llm-output-category-nonsensical | configuration-mismatch-category-tool-definition | coding-use-case-specific-failure-types-category-edge-case-oversights | coding-use-case-specific-failure-types-category-dependency-issues | other`   
Required: Yes

 ** confidence **   <a name="BedrockAgentCore-Type-InsightsFailureSignal-confidence"></a>
The confidence score of the failure detection.  
Type: Double  
Required: Yes

 ** evidence **   <a name="BedrockAgentCore-Type-InsightsFailureSignal-evidence"></a>
The evidence supporting the failure detection.  
Type: String  
Required: Yes

## See Also
<a name="API_InsightsFailureSignal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InsightsFailureSignal) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InsightsFailureSignal) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InsightsFailureSignal) 