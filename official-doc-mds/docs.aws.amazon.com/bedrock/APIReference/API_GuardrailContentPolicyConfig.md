

# GuardrailContentPolicyConfig
<a name="API_GuardrailContentPolicyConfig"></a>

Contains details about how to handle harmful content.

## Contents
<a name="API_GuardrailContentPolicyConfig_Contents"></a>

 ** filtersConfig **   <a name="bedrock-Type-GuardrailContentPolicyConfig-filtersConfig"></a>
Contains the type of the content filter and how strongly it should apply to prompts and model responses.  
Type: Array of [GuardrailContentFilterConfig](API_GuardrailContentFilterConfig.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 6 items.  
Required: Yes

 ** tierConfig **   <a name="bedrock-Type-GuardrailContentPolicyConfig-tierConfig"></a>
The tier that your guardrail uses for content filters.  
Type: [GuardrailContentFiltersTierConfig](API_GuardrailContentFiltersTierConfig.md) object  
Required: No

## See Also
<a name="API_GuardrailContentPolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailContentPolicyConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailContentPolicyConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailContentPolicyConfig) 