

# VectorIngestionConfiguration
<a name="API_agent_VectorIngestionConfiguration"></a>

Contains details about how to ingest the documents in a data source.

## Contents
<a name="API_agent_VectorIngestionConfiguration_Contents"></a>

 ** chunkingConfiguration **   <a name="bedrock-Type-agent_VectorIngestionConfiguration-chunkingConfiguration"></a>
Details about how to chunk the documents in the data source. A *chunk* refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.  
Type: [ChunkingConfiguration](API_agent_ChunkingConfiguration.md) object  
Required: No

 ** contextEnrichmentConfiguration **   <a name="bedrock-Type-agent_VectorIngestionConfiguration-contextEnrichmentConfiguration"></a>
The context enrichment configuration used for ingestion of the data into the vector store.  
Type: [ContextEnrichmentConfiguration](API_agent_ContextEnrichmentConfiguration.md) object  
Required: No

 ** customTransformationConfiguration **   <a name="bedrock-Type-agent_VectorIngestionConfiguration-customTransformationConfiguration"></a>
A custom document transformer for parsed data source documents.  
Type: [CustomTransformationConfiguration](API_agent_CustomTransformationConfiguration.md) object  
Required: No

 ** parsingConfiguration **   <a name="bedrock-Type-agent_VectorIngestionConfiguration-parsingConfiguration"></a>
Configurations for a parser to use for parsing documents in your data source. If you exclude this field, the default parser will be used.  
Type: [ParsingConfiguration](API_agent_ParsingConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_VectorIngestionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/VectorIngestionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/VectorIngestionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/VectorIngestionConfiguration) 