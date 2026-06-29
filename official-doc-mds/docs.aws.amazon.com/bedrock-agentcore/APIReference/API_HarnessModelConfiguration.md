

# HarnessModelConfiguration
<a name="API_HarnessModelConfiguration"></a>

Specification of which model to use.

## Contents
<a name="API_HarnessModelConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** bedrockModelConfig **   <a name="BedrockAgentCore-Type-HarnessModelConfiguration-bedrockModelConfig"></a>
Configuration for an Amazon Bedrock model.  
Type: [HarnessBedrockModelConfig](API_HarnessBedrockModelConfig.md) object  
Required: No

 ** geminiModelConfig **   <a name="BedrockAgentCore-Type-HarnessModelConfiguration-geminiModelConfig"></a>
Configuration for a Google Gemini model.  
Type: [HarnessGeminiModelConfig](API_HarnessGeminiModelConfig.md) object  
Required: No

 ** liteLlmModelConfig **   <a name="BedrockAgentCore-Type-HarnessModelConfiguration-liteLlmModelConfig"></a>
The LiteLLM model configuration for connecting to third-party model providers.  
Type: [HarnessLiteLlmModelConfig](API_HarnessLiteLlmModelConfig.md) object  
Required: No

 ** openAiModelConfig **   <a name="BedrockAgentCore-Type-HarnessModelConfiguration-openAiModelConfig"></a>
Configuration for an OpenAI model.  
Type: [HarnessOpenAiModelConfig](API_HarnessOpenAiModelConfig.md) object  
Required: No

## See Also
<a name="API_HarnessModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessModelConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessModelConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessModelConfiguration) 