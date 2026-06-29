

# GenerationConfiguration
<a name="API_GenerationConfiguration"></a>

The configuration details for response generation based on retrieved text chunks.

## Contents
<a name="API_GenerationConfiguration_Contents"></a>

 ** additionalModelRequestFields **   <a name="bedrock-Type-GenerationConfiguration-additionalModelRequestFields"></a>
Additional model parameters and corresponding values not included in the `textInferenceConfig` structure for a knowledge base. This allows you to provide custom model parameters specific to the language model being used.  
Type: String to JSON value map  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** guardrailConfiguration **   <a name="bedrock-Type-GenerationConfiguration-guardrailConfiguration"></a>
Contains configuration details for the guardrail.  
Type: [GuardrailConfiguration](API_GuardrailConfiguration.md) object  
Required: No

 ** kbInferenceConfig **   <a name="bedrock-Type-GenerationConfiguration-kbInferenceConfig"></a>
Contains configuration details for inference for knowledge base retrieval and response generation.  
Type: [KbInferenceConfig](API_KbInferenceConfig.md) object  
Required: No

 ** promptTemplate **   <a name="bedrock-Type-GenerationConfiguration-promptTemplate"></a>
Contains the template for the prompt that's sent to the model for response generation.  
Type: [PromptTemplate](API_PromptTemplate.md) object  
Required: No

## See Also
<a name="API_GenerationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GenerationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GenerationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GenerationConfiguration) 