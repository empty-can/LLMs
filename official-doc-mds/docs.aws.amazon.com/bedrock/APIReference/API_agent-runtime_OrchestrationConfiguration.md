

# OrchestrationConfiguration
<a name="API_agent-runtime_OrchestrationConfiguration"></a>

Settings for how the model processes the prompt prior to retrieval and generation.

## Contents
<a name="API_agent-runtime_OrchestrationConfiguration_Contents"></a>

 ** additionalModelRequestFields **   <a name="bedrock-Type-agent-runtime_OrchestrationConfiguration-additionalModelRequestFields"></a>
 Additional model parameters and corresponding values not included in the textInferenceConfig structure for a knowledge base. This allows users to provide custom model parameters specific to the language model being used.   
Type: String to JSON value map  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** inferenceConfig **   <a name="bedrock-Type-agent-runtime_OrchestrationConfiguration-inferenceConfig"></a>
 Configuration settings for inference when using RetrieveAndGenerate to generate responses while using a knowledge base as a source.   
Type: [InferenceConfig](API_agent-runtime_InferenceConfig.md) object  
Required: No

 ** performanceConfig **   <a name="bedrock-Type-agent-runtime_OrchestrationConfiguration-performanceConfig"></a>
The latency configuration for the model.  
Type: [PerformanceConfiguration](API_agent-runtime_PerformanceConfiguration.md) object  
Required: No

 ** promptTemplate **   <a name="bedrock-Type-agent-runtime_OrchestrationConfiguration-promptTemplate"></a>
Contains the template for the prompt that's sent to the model. Orchestration prompts must include the `$conversation_history$` and `$output_format_instructions$` variables. For more information, see [Use placeholder variables](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-placeholders.html) in the user guide.  
Type: [PromptTemplate](API_agent-runtime_PromptTemplate.md) object  
Required: No

 ** queryTransformationConfiguration **   <a name="bedrock-Type-agent-runtime_OrchestrationConfiguration-queryTransformationConfiguration"></a>
To split up the prompt and retrieve multiple sources, set the transformation type to `QUERY_DECOMPOSITION`.  
Type: [QueryTransformationConfiguration](API_agent-runtime_QueryTransformationConfiguration.md) object  
Required: No

## See Also
<a name="API_agent-runtime_OrchestrationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/OrchestrationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/OrchestrationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/OrchestrationConfiguration) 