

# GuardrailStreamConfiguration
<a name="API_runtime_GuardrailStreamConfiguration"></a>

Configuration information for a guardrail that you use with the [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) action. 

## Contents
<a name="API_runtime_GuardrailStreamConfiguration_Contents"></a>

 ** guardrailIdentifier **   <a name="bedrock-Type-runtime_GuardrailStreamConfiguration-guardrailIdentifier"></a>
The identifier for the guardrail.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `(|([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))`   
Required: No

 ** guardrailVersion **   <a name="bedrock-Type-runtime_GuardrailStreamConfiguration-guardrailVersion"></a>
The version of the guardrail.  
Type: String  
Pattern: `(|([1-9][0-9]{0,7})|(DRAFT))`   
Required: No

 ** streamProcessingMode **   <a name="bedrock-Type-runtime_GuardrailStreamConfiguration-streamProcessingMode"></a>
The processing mode.   
The processing mode. For more information, see [Configure streaming response behavior](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html).   
Type: String  
Valid Values: `sync | async`   
Required: No

 ** trace **   <a name="bedrock-Type-runtime_GuardrailStreamConfiguration-trace"></a>
The trace behavior for the guardrail.  
Type: String  
Valid Values: `enabled | disabled | enabled_full`   
Required: No

## See Also
<a name="API_runtime_GuardrailStreamConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailStreamConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailStreamConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailStreamConfiguration) 