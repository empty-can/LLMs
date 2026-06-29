

# GuardrailConfiguration
<a name="API_runtime_GuardrailConfiguration"></a>

Configuration information for a guardrail that you use with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) operation.

## Contents
<a name="API_runtime_GuardrailConfiguration_Contents"></a>

 ** guardrailIdentifier **   <a name="bedrock-Type-runtime_GuardrailConfiguration-guardrailIdentifier"></a>
The identifier for the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(|([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`   
Required: No

 ** guardrailVersion **   <a name="bedrock-Type-runtime_GuardrailConfiguration-guardrailVersion"></a>
The version of the guardrail.  
Type: String  
Pattern: `(|([1-9][0-9]{0,7})|(DRAFT))`   
Required: No

 ** trace **   <a name="bedrock-Type-runtime_GuardrailConfiguration-trace"></a>
The trace behavior for the guardrail.  
Type: String  
Valid Values: `enabled | disabled | enabled_full`   
Required: No

## See Also
<a name="API_runtime_GuardrailConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailConfiguration) 