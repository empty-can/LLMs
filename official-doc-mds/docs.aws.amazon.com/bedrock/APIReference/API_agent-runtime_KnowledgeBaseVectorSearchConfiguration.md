

# KnowledgeBaseVectorSearchConfiguration
<a name="API_agent-runtime_KnowledgeBaseVectorSearchConfiguration"></a>

Configurations for how to perform the search query and return results. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).

This data type is used in the following API operations:
+  [Retrieve request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_RequestSyntax) – in the `vectorSearchConfiguration` field
+  [RetrieveAndGenerate request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_RequestSyntax) – in the `vectorSearchConfiguration` field

## Contents
<a name="API_agent-runtime_KnowledgeBaseVectorSearchConfiguration_Contents"></a>

 ** filter **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseVectorSearchConfiguration-filter"></a>
Specifies the filters to use on the metadata in the knowledge base data sources before returning results. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).  
Type: [RetrievalFilter](API_agent-runtime_RetrievalFilter.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** implicitFilterConfiguration **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseVectorSearchConfiguration-implicitFilterConfiguration"></a>
Settings for implicit filtering.  
Type: [ImplicitFilterConfiguration](API_agent-runtime_ImplicitFilterConfiguration.md) object  
Required: No

 ** numberOfResults **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseVectorSearchConfiguration-numberOfResults"></a>
The number of source chunks to retrieve.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** overrideSearchType **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseVectorSearchConfiguration-overrideSearchType"></a>
By default, Amazon Bedrock decides a search strategy for you. If you're using an Amazon OpenSearch Serverless vector store that contains a filterable text field, you can specify whether to query the knowledge base with a `HYBRID` search using both vector embeddings and raw text, or `SEMANTIC` search using only vector embeddings. For other vector store configurations, only `SEMANTIC` search is available. For more information, see [Test a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-test.html).  
Type: String  
Valid Values: `HYBRID | SEMANTIC`   
Required: No

 ** rerankingConfiguration **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseVectorSearchConfiguration-rerankingConfiguration"></a>
Contains configurations for reranking the retrieved results. For more information, see [Improve the relevance of query responses with a reranker model](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html).  
Type: [VectorSearchRerankingConfiguration](API_agent-runtime_VectorSearchRerankingConfiguration.md) object  
Required: No

## See Also
<a name="API_agent-runtime_KnowledgeBaseVectorSearchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/KnowledgeBaseVectorSearchConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/KnowledgeBaseVectorSearchConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/KnowledgeBaseVectorSearchConfiguration) 