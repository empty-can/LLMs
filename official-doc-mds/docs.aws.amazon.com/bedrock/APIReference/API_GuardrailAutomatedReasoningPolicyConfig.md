

# GuardrailAutomatedReasoningPolicyConfig
<a name="API_GuardrailAutomatedReasoningPolicyConfig"></a>

Configuration settings for integrating Automated Reasoning policies with Amazon Bedrock Guardrails.

## Contents
<a name="API_GuardrailAutomatedReasoningPolicyConfig_Contents"></a>

 ** policies **   <a name="bedrock-Type-GuardrailAutomatedReasoningPolicyConfig-policies"></a>
The list of Automated Reasoning policy ARNs to include in the guardrail configuration.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

 ** confidenceThreshold **   <a name="bedrock-Type-GuardrailAutomatedReasoningPolicyConfig-confidenceThreshold"></a>
The confidence threshold for triggering guardrail actions based on Automated Reasoning policy violations.  
Type: Double  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

## See Also
<a name="API_GuardrailAutomatedReasoningPolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailAutomatedReasoningPolicyConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailAutomatedReasoningPolicyConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailAutomatedReasoningPolicyConfig) 