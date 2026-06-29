

# CitationsDelta
<a name="API_runtime_CitationsDelta"></a>

Contains incremental updates to citation information during streaming responses. This allows clients to build up citation data progressively as the response is generated.

## Contents
<a name="API_runtime_CitationsDelta_Contents"></a>

 ** location **   <a name="bedrock-Type-runtime_CitationsDelta-location"></a>
Specifies the precise location within a source document where cited content can be found. This can include character-level positions, page numbers, or document chunks depending on the document type and indexing method.  
Type: [CitationLocation](API_runtime_CitationLocation.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** source **   <a name="bedrock-Type-runtime_CitationsDelta-source"></a>
The source from the original search result that provided the cited content.  
Type: String  
Required: No

 ** sourceContent **   <a name="bedrock-Type-runtime_CitationsDelta-sourceContent"></a>
The specific content from the source document that was referenced or cited in the generated response.  
Type: Array of [CitationSourceContentDelta](API_runtime_CitationSourceContentDelta.md) objects  
Required: No

 ** title **   <a name="bedrock-Type-runtime_CitationsDelta-title"></a>
The title or identifier of the source document being cited.  
Type: String  
Required: No

## See Also
<a name="API_runtime_CitationsDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/CitationsDelta) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/CitationsDelta) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/CitationsDelta) 