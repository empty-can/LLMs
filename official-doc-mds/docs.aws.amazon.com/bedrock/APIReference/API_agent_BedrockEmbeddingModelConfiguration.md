

# BedrockEmbeddingModelConfiguration
<a name="API_agent_BedrockEmbeddingModelConfiguration"></a>

The vector configuration details for the Bedrock embeddings model.

## Contents
<a name="API_agent_BedrockEmbeddingModelConfiguration_Contents"></a>

 ** audio **   <a name="bedrock-Type-agent_BedrockEmbeddingModelConfiguration-audio"></a>
Configuration settings for processing audio content in multimodal knowledge bases.  
Type: Array of [AudioConfiguration](API_agent_AudioConfiguration.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

 ** dimensions **   <a name="bedrock-Type-agent_BedrockEmbeddingModelConfiguration-dimensions"></a>
The dimensions details for the vector configuration used on the Bedrock embeddings model.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 4096.  
Required: No

 ** embeddingDataType **   <a name="bedrock-Type-agent_BedrockEmbeddingModelConfiguration-embeddingDataType"></a>
The data type for the vectors when using a model to convert text into vector embeddings. The model must support the specified data type for vector embeddings. Floating-point (float32) is the default data type, and is supported by most models for vector embeddings. See [Supported embeddings models](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html) for information on the available models and their vector data types.  
Type: String  
Valid Values: `FLOAT32 | BINARY`   
Required: No

 ** video **   <a name="bedrock-Type-agent_BedrockEmbeddingModelConfiguration-video"></a>
Configuration settings for processing video content in multimodal knowledge bases.  
Type: Array of [VideoConfiguration](API_agent_VideoConfiguration.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

## See Also
<a name="API_agent_BedrockEmbeddingModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/BedrockEmbeddingModelConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/BedrockEmbeddingModelConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/BedrockEmbeddingModelConfiguration) 