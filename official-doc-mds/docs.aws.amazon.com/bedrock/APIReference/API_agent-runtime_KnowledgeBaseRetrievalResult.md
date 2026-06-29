

# KnowledgeBaseRetrievalResult
<a name="API_agent-runtime_KnowledgeBaseRetrievalResult"></a>

Details about a result from querying the knowledge base.

This data type is used in the following API operations:
+  [Retrieve response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_ResponseSyntax) – in the `retrievalResults` field

## Contents
<a name="API_agent-runtime_KnowledgeBaseRetrievalResult_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrievalResult-content"></a>
Contains information about the content of the chunk.  
Type: [RetrievalResultContent](API_agent-runtime_RetrievalResultContent.md) object  
Required: Yes

 ** documentId **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrievalResult-documentId"></a>
The unique identifier of the document. Use with `GetDocumentContent` to retrieve the full document.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1825.  
Pattern: `\P{C}*`   
Required: No

 ** location **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrievalResult-location"></a>
Contains information about the location of the data source.  
Type: [RetrievalResultLocation](API_agent-runtime_RetrievalResultLocation.md) object  
Required: No

 ** metadata **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrievalResult-metadata"></a>
Contains metadata attributes and their values for the file in the data source. For more information, see [Metadata and filtering](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html#kb-ds-metadata).  
Type: String to JSON value map  
Map Entries: Maximum number of items.  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** score **   <a name="bedrock-Type-agent-runtime_KnowledgeBaseRetrievalResult-score"></a>
The level of relevance of the result to the query.  
Type: Double  
Required: No

## See Also
<a name="API_agent-runtime_KnowledgeBaseRetrievalResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrievalResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrievalResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/KnowledgeBaseRetrievalResult) 