

# KnowledgeBaseVectorSearchConfiguration
<a name="API_KnowledgeBaseVectorSearchConfiguration"></a>

The configuration details for returning the results from the knowledge base vector search.

## Contents
<a name="API_KnowledgeBaseVectorSearchConfiguration_Contents"></a>

 ** filter **   <a name="bedrock-Type-KnowledgeBaseVectorSearchConfiguration-filter"></a>
Specifies the filters to use on the metadata fields in the knowledge base data sources before returning results.  
Type: [RetrievalFilter](API_RetrievalFilter.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** implicitFilterConfiguration **   <a name="bedrock-Type-KnowledgeBaseVectorSearchConfiguration-implicitFilterConfiguration"></a>
Configuration for implicit filtering in Knowledge Base vector searches. This allows the system to automatically apply filters based on the query context without requiring explicit filter expressions.  
Type: [ImplicitFilterConfiguration](API_ImplicitFilterConfiguration.md) object  
Required: No

 ** numberOfResults **   <a name="bedrock-Type-KnowledgeBaseVectorSearchConfiguration-numberOfResults"></a>
The number of text chunks to retrieve; the number of results to return.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** overrideSearchType **   <a name="bedrock-Type-KnowledgeBaseVectorSearchConfiguration-overrideSearchType"></a>
By default, Amazon Bedrock decides a search strategy for you. If you're using an Amazon OpenSearch Serverless vector store that contains a filterable text field, you can specify whether to query the knowledge base with a `HYBRID` search using both vector embeddings and raw text, or `SEMANTIC` search using only vector embeddings. For other vector store configurations, only `SEMANTIC` search is available.  
Type: String  
Valid Values: `HYBRID | SEMANTIC`   
Required: No

 ** rerankingConfiguration **   <a name="bedrock-Type-KnowledgeBaseVectorSearchConfiguration-rerankingConfiguration"></a>
Configuration for reranking search results in Knowledge Base vector searches. Reranking improves search relevance by reordering initial vector search results using more sophisticated relevance models.  
Type: [VectorSearchRerankingConfiguration](API_VectorSearchRerankingConfiguration.md) object  
Required: No

## See Also
<a name="API_KnowledgeBaseVectorSearchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/KnowledgeBaseVectorSearchConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/KnowledgeBaseVectorSearchConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/KnowledgeBaseVectorSearchConfiguration) 