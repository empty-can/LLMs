

# ExternalSourcesGenerationConfiguration
<a name="API_agent-runtime_ExternalSourcesGenerationConfiguration"></a>

Contains the generation configuration of the external source wrapper object.

## Contents
<a name="API_agent-runtime_ExternalSourcesGenerationConfiguration_Contents"></a>

 ** additionalModelRequestFields **   <a name="bedrock-Type-agent-runtime_ExternalSourcesGenerationConfiguration-additionalModelRequestFields"></a>
 Additional model parameters and their corresponding values not included in the textInferenceConfig structure for an external source. Takes in custom model parameters specific to the language model being used.   
Type: String to JSON value map  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** guardrailConfiguration **   <a name="bedrock-Type-agent-runtime_ExternalSourcesGenerationConfiguration-guardrailConfiguration"></a>
The configuration details for the guardrail.  
Type: [GuardrailConfiguration](API_agent-runtime_GuardrailConfiguration.md) object  
Required: No

 ** inferenceConfig **   <a name="bedrock-Type-agent-runtime_ExternalSourcesGenerationConfiguration-inferenceConfig"></a>
 Configuration settings for inference when using RetrieveAndGenerate to generate responses while using an external source.  
Type: [InferenceConfig](API_agent-runtime_InferenceConfig.md) object  
Required: No

 ** performanceConfig **   <a name="bedrock-Type-agent-runtime_ExternalSourcesGenerationConfiguration-performanceConfig"></a>
The latency configuration for the model.  
Type: [PerformanceConfiguration](API_agent-runtime_PerformanceConfiguration.md) object  
Required: No

 ** promptTemplate **   <a name="bedrock-Type-agent-runtime_ExternalSourcesGenerationConfiguration-promptTemplate"></a>
Contain the textPromptTemplate string for the external source wrapper object.  
Type: [PromptTemplate](API_agent-runtime_PromptTemplate.md) object  
Required: No

## See Also
<a name="API_agent-runtime_ExternalSourcesGenerationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ExternalSourcesGenerationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ExternalSourcesGenerationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ExternalSourcesGenerationConfiguration) 