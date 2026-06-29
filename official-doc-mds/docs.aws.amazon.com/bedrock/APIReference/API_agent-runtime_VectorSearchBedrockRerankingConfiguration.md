

# VectorSearchBedrockRerankingConfiguration
<a name="API_agent-runtime_VectorSearchBedrockRerankingConfiguration"></a>

Contains configurations for reranking with an Amazon Bedrock reranker model.

## Contents
<a name="API_agent-runtime_VectorSearchBedrockRerankingConfiguration_Contents"></a>

 ** modelConfiguration **   <a name="bedrock-Type-agent-runtime_VectorSearchBedrockRerankingConfiguration-modelConfiguration"></a>
Contains configurations for the reranker model.  
Type: [VectorSearchBedrockRerankingModelConfiguration](API_agent-runtime_VectorSearchBedrockRerankingModelConfiguration.md) object  
Required: Yes

 ** metadataConfiguration **   <a name="bedrock-Type-agent-runtime_VectorSearchBedrockRerankingConfiguration-metadataConfiguration"></a>
Contains configurations for the metadata to use in reranking.  
Type: [MetadataConfigurationForReranking](API_agent-runtime_MetadataConfigurationForReranking.md) object  
Required: No

 ** numberOfRerankedResults **   <a name="bedrock-Type-agent-runtime_VectorSearchBedrockRerankingConfiguration-numberOfRerankedResults"></a>
The number of results to return after reranking.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

## See Also
<a name="API_agent-runtime_VectorSearchBedrockRerankingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/VectorSearchBedrockRerankingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/VectorSearchBedrockRerankingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/VectorSearchBedrockRerankingConfiguration) 