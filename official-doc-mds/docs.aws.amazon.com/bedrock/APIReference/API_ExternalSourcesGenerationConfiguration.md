

# ExternalSourcesGenerationConfiguration
<a name="API_ExternalSourcesGenerationConfiguration"></a>

The response generation configuration of the external source wrapper object.

## Contents
<a name="API_ExternalSourcesGenerationConfiguration_Contents"></a>

 ** additionalModelRequestFields **   <a name="bedrock-Type-ExternalSourcesGenerationConfiguration-additionalModelRequestFields"></a>
Additional model parameters and their corresponding values not included in the text inference configuration for an external source. Takes in custom model parameters specific to the language model being used.  
Type: String to JSON value map  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** guardrailConfiguration **   <a name="bedrock-Type-ExternalSourcesGenerationConfiguration-guardrailConfiguration"></a>
Configuration details for the guardrail.  
Type: [GuardrailConfiguration](API_GuardrailConfiguration.md) object  
Required: No

 ** kbInferenceConfig **   <a name="bedrock-Type-ExternalSourcesGenerationConfiguration-kbInferenceConfig"></a>
Configuration details for inference when using `RetrieveAndGenerate` to generate responses while using an external source.  
Type: [KbInferenceConfig](API_KbInferenceConfig.md) object  
Required: No

 ** promptTemplate **   <a name="bedrock-Type-ExternalSourcesGenerationConfiguration-promptTemplate"></a>
Contains the template for the prompt for the external source wrapper object.  
Type: [PromptTemplate](API_PromptTemplate.md) object  
Required: No

## See Also
<a name="API_ExternalSourcesGenerationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ExternalSourcesGenerationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ExternalSourcesGenerationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ExternalSourcesGenerationConfiguration) 