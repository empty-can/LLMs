

# CitationLocation
<a name="API_runtime_CitationLocation"></a>

Specifies the precise location within a source document where cited content can be found. This can include character-level positions, page numbers, or document chunks depending on the document type and indexing method.

## Contents
<a name="API_runtime_CitationLocation_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** documentChar **   <a name="bedrock-Type-runtime_CitationLocation-documentChar"></a>
The character-level location within the document where the cited content is found.  
Type: [DocumentCharLocation](API_runtime_DocumentCharLocation.md) object  
Required: No

 ** documentChunk **   <a name="bedrock-Type-runtime_CitationLocation-documentChunk"></a>
The chunk-level location within the document where the cited content is found, typically used for documents that have been segmented into logical chunks.  
Type: [DocumentChunkLocation](API_runtime_DocumentChunkLocation.md) object  
Required: No

 ** documentPage **   <a name="bedrock-Type-runtime_CitationLocation-documentPage"></a>
The page-level location within the document where the cited content is found.  
Type: [DocumentPageLocation](API_runtime_DocumentPageLocation.md) object  
Required: No

 ** searchResultLocation **   <a name="bedrock-Type-runtime_CitationLocation-searchResultLocation"></a>
The search result location where the cited content is found, including the search result index and block positions within the content array.  
Type: [SearchResultLocation](API_runtime_SearchResultLocation.md) object  
Required: No

 ** web **   <a name="bedrock-Type-runtime_CitationLocation-web"></a>
The web URL that was cited for this reference.  
Type: [WebLocation](API_runtime_WebLocation.md) object  
Required: No

## See Also
<a name="API_runtime_CitationLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/CitationLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/CitationLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/CitationLocation) 