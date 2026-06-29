

# GuardrailSensitiveInformationPolicyConfig
<a name="API_GuardrailSensitiveInformationPolicyConfig"></a>

Contains details about PII entities and regular expressions to configure for the guardrail.

## Contents
<a name="API_GuardrailSensitiveInformationPolicyConfig_Contents"></a>

 ** piiEntitiesConfig **   <a name="bedrock-Type-GuardrailSensitiveInformationPolicyConfig-piiEntitiesConfig"></a>
A list of PII entities to configure to the guardrail.  
Type: Array of [GuardrailPiiEntityConfig](API_GuardrailPiiEntityConfig.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

 ** regexesConfig **   <a name="bedrock-Type-GuardrailSensitiveInformationPolicyConfig-regexesConfig"></a>
A list of regular expressions to configure to the guardrail.  
Type: Array of [GuardrailRegexConfig](API_GuardrailRegexConfig.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 30 items.  
Required: No

## See Also
<a name="API_GuardrailSensitiveInformationPolicyConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GuardrailSensitiveInformationPolicyConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GuardrailSensitiveInformationPolicyConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GuardrailSensitiveInformationPolicyConfig) 