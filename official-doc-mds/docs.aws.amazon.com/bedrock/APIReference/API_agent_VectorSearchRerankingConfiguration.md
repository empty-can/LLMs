

# VectorSearchRerankingConfiguration
<a name="API_agent_VectorSearchRerankingConfiguration"></a>

Specifies how retrieved results from a knowledge base are reranked to improve relevance.

## Contents
<a name="API_agent_VectorSearchRerankingConfiguration_Contents"></a>

 ** type **   <a name="bedrock-Type-agent_VectorSearchRerankingConfiguration-type"></a>
Specifies the type of reranking model to use. Currently, the only supported value is `BEDROCK_RERANKING_MODEL`.  
Type: String  
Valid Values: `BEDROCK_RERANKING_MODEL`   
Required: Yes

 ** bedrockRerankingConfiguration **   <a name="bedrock-Type-agent_VectorSearchRerankingConfiguration-bedrockRerankingConfiguration"></a>
Specifies the configuration for using an Amazon Bedrock reranker model to rerank retrieved results.  
Type: [VectorSearchBedrockRerankingConfiguration](API_agent_VectorSearchBedrockRerankingConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_VectorSearchRerankingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/VectorSearchRerankingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/VectorSearchRerankingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/VectorSearchRerankingConfiguration) 