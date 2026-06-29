

# GenerationConfiguration
<a name="API_agent-runtime_GenerationConfiguration"></a>

Contains configurations for response generation based on the knowledge base query results.

This data type is used in the following API operations:
+  [RetrieveAndGenerate request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_RequestSyntax) 

## Contents
<a name="API_agent-runtime_GenerationConfiguration_Contents"></a>

 ** additionalModelRequestFields **   <a name="bedrock-Type-agent-runtime_GenerationConfiguration-additionalModelRequestFields"></a>
 Additional model parameters and corresponding values not included in the textInferenceConfig structure for a knowledge base. This allows users to provide custom model parameters specific to the language model being used.   
Type: String to JSON value map  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** guardrailConfiguration **   <a name="bedrock-Type-agent-runtime_GenerationConfiguration-guardrailConfiguration"></a>
The configuration details for the guardrail.  
Type: [GuardrailConfiguration](API_agent-runtime_GuardrailConfiguration.md) object  
Required: No

 ** inferenceConfig **   <a name="bedrock-Type-agent-runtime_GenerationConfiguration-inferenceConfig"></a>
 Configuration settings for inference when using RetrieveAndGenerate to generate responses while using a knowledge base as a source.   
Type: [InferenceConfig](API_agent-runtime_InferenceConfig.md) object  
Required: No

 ** performanceConfig **   <a name="bedrock-Type-agent-runtime_GenerationConfiguration-performanceConfig"></a>
The latency configuration for the model.  
Type: [PerformanceConfiguration](API_agent-runtime_PerformanceConfiguration.md) object  
Required: No

 ** promptTemplate **   <a name="bedrock-Type-agent-runtime_GenerationConfiguration-promptTemplate"></a>
Contains the template for the prompt that's sent to the model for response generation. Generation prompts must include the `$search_results$` variable. For more information, see [Use placeholder variables](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-placeholders.html) in the user guide.  
Type: [PromptTemplate](API_agent-runtime_PromptTemplate.md) object  
Required: No

## See Also
<a name="API_agent-runtime_GenerationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/GenerationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/GenerationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/GenerationConfiguration) 