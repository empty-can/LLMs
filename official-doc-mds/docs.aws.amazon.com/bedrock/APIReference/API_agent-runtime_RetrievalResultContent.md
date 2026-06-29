

# RetrievalResultContent
<a name="API_agent-runtime_RetrievalResultContent"></a>

Contains information about a chunk of text from a data source in the knowledge base. If the result is from a structured data source, the cell in the database and the type of the value is also identified.

This data type is used in the following API operations:
+  [Retrieve response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_ResponseSyntax) – in the `content` field
+  [RetrieveAndGenerate response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_ResponseSyntax) – in the `content` field
+  [InvokeAgent response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html#API_agent-runtime_InvokeAgent_ResponseSyntax) – in the `content` field

## Contents
<a name="API_agent-runtime_RetrievalResultContent_Contents"></a>

 ** audio **   <a name="bedrock-Type-agent-runtime_RetrievalResultContent-audio"></a>
Audio segment information when the retrieval result contains audio content.  
Type: [AudioSegment](API_agent-runtime_AudioSegment.md) object  
Required: No

 ** byteContent **   <a name="bedrock-Type-agent-runtime_RetrievalResultContent-byteContent"></a>
A data URI with base64-encoded content from the data source. The URI is in the following format: returned in the following format: `data:image/jpeg;base64,${base64-encoded string}`.  
Type: String  
Required: No

 ** row **   <a name="bedrock-Type-agent-runtime_RetrievalResultContent-row"></a>
Specifies information about the rows with the cells to return in retrieval.  
Type: Array of [RetrievalResultContentColumn](API_agent-runtime_RetrievalResultContentColumn.md) objects  
Required: No

 ** text **   <a name="bedrock-Type-agent-runtime_RetrievalResultContent-text"></a>
The cited text from the data source.  
Type: String  
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_RetrievalResultContent-type"></a>
The type of content in the retrieval result.  
Type: String  
Valid Values: `TEXT | IMAGE | ROW | AUDIO | VIDEO`   
Required: No

 ** video **   <a name="bedrock-Type-agent-runtime_RetrievalResultContent-video"></a>
Video segment information when the retrieval result contains video content.  
Type: [VideoSegment](API_agent-runtime_VideoSegment.md) object  
Required: No

## See Also
<a name="API_agent-runtime_RetrievalResultContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RetrievalResultContent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RetrievalResultContent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RetrievalResultContent) 