

# Citation
<a name="API_runtime_Citation"></a>

Contains information about a citation that references a specific source document. Citations provide traceability between the model's generated response and the source documents that informed that response.

## Contents
<a name="API_runtime_Citation_Contents"></a>

 ** location **   <a name="bedrock-Type-runtime_Citation-location"></a>
The precise location within the source document where the cited content can be found, including character positions, page numbers, or chunk identifiers.  
Type: [CitationLocation](API_runtime_CitationLocation.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** source **   <a name="bedrock-Type-runtime_Citation-source"></a>
The source from the original search result that provided the cited content.  
Type: String  
Required: No

 ** sourceContent **   <a name="bedrock-Type-runtime_Citation-sourceContent"></a>
The specific content from the source document that was referenced or cited in the generated response.  
Type: Array of [CitationSourceContent](API_runtime_CitationSourceContent.md) objects  
Required: No

 ** title **   <a name="bedrock-Type-runtime_Citation-title"></a>
The title or identifier of the source document being cited.  
Type: String  
Required: No

## See Also
<a name="API_runtime_Citation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/Citation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/Citation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/Citation) 