

# VectorSearchBedrockRerankingConfiguration
<a name="API_VectorSearchBedrockRerankingConfiguration"></a>

Configuration for using Amazon Bedrock foundation models to rerank Knowledge Base vector search results. This enables more sophisticated relevance ranking using large language models.

## Contents
<a name="API_VectorSearchBedrockRerankingConfiguration_Contents"></a>

 ** modelConfiguration **   <a name="bedrock-Type-VectorSearchBedrockRerankingConfiguration-modelConfiguration"></a>
Configuration for the Amazon Bedrock foundation model used for reranking. This includes the model ARN and any additional request fields required by the model.  
Type: [VectorSearchBedrockRerankingModelConfiguration](API_VectorSearchBedrockRerankingModelConfiguration.md) object  
Required: Yes

 ** metadataConfiguration **   <a name="bedrock-Type-VectorSearchBedrockRerankingConfiguration-metadataConfiguration"></a>
Configuration for how document metadata should be used during the reranking process. This determines which metadata fields are included when reordering search results.  
Type: [MetadataConfigurationForReranking](API_MetadataConfigurationForReranking.md) object  
Required: No

 ** numberOfRerankedResults **   <a name="bedrock-Type-VectorSearchBedrockRerankingConfiguration-numberOfRerankedResults"></a>
The maximum number of results to rerank. This limits how many of the initial vector search results will be processed by the reranking model. A smaller number improves performance but may exclude potentially relevant results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

## See Also
<a name="API_VectorSearchBedrockRerankingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/VectorSearchBedrockRerankingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/VectorSearchBedrockRerankingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/VectorSearchBedrockRerankingConfiguration) 