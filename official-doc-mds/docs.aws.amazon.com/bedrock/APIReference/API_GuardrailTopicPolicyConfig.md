

# GuardrailTopicPolicyConfig
<a name="API_GuardrailTopicPolicyConfig"></a>

Contains details about topics that the guardrail should identify and deny.

## Contents
<a name="API_GuardrailTopicPolicyConfig_Contents"></a>

 ** topicsConfig **   <a name="bedrock-Type-GuardrailTopicPolicyConfig-topicsConfig"></a>
A list of policies related to topics that the guardrail should deny.  
Type: Array of [GuardrailTopicConfig](API_GuardrailTopicConfig.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 30 items.  
Required: Yes

 ** tierConfig **   <a name="bedrock-Type-GuardrailTopicPolicyConfig-tierConfig"></a>
The tier that your guardrail uses for denied topic filters.  
Type: [GuardrailTopicsTierConfig](API_GuardrailTopicsTierConfig.md) object  
Required: No

## See Also
<a name="API_GuardrailTopicPolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailTopicPolicyConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailTopicPolicyConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailTopicPolicyConfig) 