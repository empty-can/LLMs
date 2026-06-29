

# VectorSearchBedrockRerankingConfiguration
<a name="API_agent_VectorSearchBedrockRerankingConfiguration"></a>

Configures the Amazon Bedrock reranker model to improve the relevance of retrieved results.

## Contents
<a name="API_agent_VectorSearchBedrockRerankingConfiguration_Contents"></a>

 ** modelConfiguration **   <a name="bedrock-Type-agent_VectorSearchBedrockRerankingConfiguration-modelConfiguration"></a>
Specifies the configuration for the Amazon Bedrock reranker model.  
Type: [VectorSearchBedrockRerankingModelConfiguration](API_agent_VectorSearchBedrockRerankingModelConfiguration.md) object  
Required: Yes

 ** metadataConfiguration **   <a name="bedrock-Type-agent_VectorSearchBedrockRerankingConfiguration-metadataConfiguration"></a>
Specifies how metadata fields should be handled during the reranking process.  
Type: [MetadataConfigurationForReranking](API_agent_MetadataConfigurationForReranking.md) object  
Required: No

 ** numberOfRerankedResults **   <a name="bedrock-Type-agent_VectorSearchBedrockRerankingConfiguration-numberOfRerankedResults"></a>
Specifies the number of results to return after reranking.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

## See Also
<a name="API_agent_VectorSearchBedrockRerankingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/VectorSearchBedrockRerankingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/VectorSearchBedrockRerankingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/VectorSearchBedrockRerankingConfiguration) 