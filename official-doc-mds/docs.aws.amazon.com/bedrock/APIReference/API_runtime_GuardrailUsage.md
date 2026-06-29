

# GuardrailUsage
<a name="API_runtime_GuardrailUsage"></a>

The details on the use of the guardrail.

## Contents
<a name="API_runtime_GuardrailUsage_Contents"></a>

 ** contentPolicyUnits **   <a name="bedrock-Type-runtime_GuardrailUsage-contentPolicyUnits"></a>
The content policy units processed by the guardrail.  
Type: Integer  
Required: Yes

 ** contextualGroundingPolicyUnits **   <a name="bedrock-Type-runtime_GuardrailUsage-contextualGroundingPolicyUnits"></a>
The contextual grounding policy units processed by the guardrail.  
Type: Integer  
Required: Yes

 ** sensitiveInformationPolicyFreeUnits **   <a name="bedrock-Type-runtime_GuardrailUsage-sensitiveInformationPolicyFreeUnits"></a>
The sensitive information policy free units processed by the guardrail.  
Type: Integer  
Required: Yes

 ** sensitiveInformationPolicyUnits **   <a name="bedrock-Type-runtime_GuardrailUsage-sensitiveInformationPolicyUnits"></a>
The sensitive information policy units processed by the guardrail.  
Type: Integer  
Required: Yes

 ** topicPolicyUnits **   <a name="bedrock-Type-runtime_GuardrailUsage-topicPolicyUnits"></a>
The topic policy units processed by the guardrail.  
Type: Integer  
Required: Yes

 ** wordPolicyUnits **   <a name="bedrock-Type-runtime_GuardrailUsage-wordPolicyUnits"></a>
The word policy units processed by the guardrail.  
Type: Integer  
Required: Yes

 ** automatedReasoningPolicies **   <a name="bedrock-Type-runtime_GuardrailUsage-automatedReasoningPolicies"></a>
The number of automated reasoning policies that were processed during the guardrail evaluation.  
Type: Integer  
Required: No

 ** automatedReasoningPolicyUnits **   <a name="bedrock-Type-runtime_GuardrailUsage-automatedReasoningPolicyUnits"></a>
The number of text units processed by the automated reasoning policy.  
Type: Integer  
Required: No

 ** contentPolicyImageUnits **   <a name="bedrock-Type-runtime_GuardrailUsage-contentPolicyImageUnits"></a>
The content policy image units processed by the guardrail.  
Type: Integer  
Required: No

## See Also
<a name="API_runtime_GuardrailUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailUsage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailUsage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailUsage) 