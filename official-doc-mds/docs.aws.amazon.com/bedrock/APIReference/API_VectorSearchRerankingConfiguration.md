

# VectorSearchRerankingConfiguration
<a name="API_VectorSearchRerankingConfiguration"></a>

Configuration for reranking vector search results to improve relevance. Reranking applies additional relevance models to reorder the initial vector search results based on more sophisticated criteria.

## Contents
<a name="API_VectorSearchRerankingConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-VectorSearchRerankingConfiguration-type"></a>
The type of reranking to apply to vector search results. Currently, the only supported value is BEDROCK, which uses Amazon Bedrock foundation models for reranking.  
Type: String  
Valid Values: `BEDROCK_RERANKING_MODEL`   
Required: Yes

 ** bedrockRerankingConfiguration **   <a name="bedrock-Type-VectorSearchRerankingConfiguration-bedrockRerankingConfiguration"></a>
Configuration for using Amazon Bedrock foundation models to rerank search results. This is required when the reranking type is set to BEDROCK.  
Type: [VectorSearchBedrockRerankingConfiguration](API_VectorSearchBedrockRerankingConfiguration.md) object  
Required: No

## See Also
<a name="API_VectorSearchRerankingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/VectorSearchRerankingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/VectorSearchRerankingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/VectorSearchRerankingConfiguration) 