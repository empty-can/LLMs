

# SearchResultBlock
<a name="API_runtime_SearchResultBlock"></a>

A search result block that enables natural citations with proper source attribution for retrieved content.

**Note**  
This field is only supported by Anthropic Claude Opus 4.1, Opus 4, Sonnet 4.5, Sonnet 4, Sonnet 3.7, and 3.5 Haiku models.

## Contents
<a name="API_runtime_SearchResultBlock_Contents"></a>

 ** content **   <a name="bedrock-Type-runtime_SearchResultBlock-content"></a>
An array of search result content block.  
Type: Array of [SearchResultContentBlock](API_runtime_SearchResultContentBlock.md) objects  
Required: Yes

 ** source **   <a name="bedrock-Type-runtime_SearchResultBlock-source"></a>
The source URL or identifier for the content.  
Type: String  
Required: Yes

 ** title **   <a name="bedrock-Type-runtime_SearchResultBlock-title"></a>
A descriptive title for the search result.  
Type: String  
Required: Yes

 ** citations **   <a name="bedrock-Type-runtime_SearchResultBlock-citations"></a>
Configuration setting for citations  
Type: [CitationsConfig](API_runtime_CitationsConfig.md) object  
Required: No

## See Also
<a name="API_runtime_SearchResultBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/SearchResultBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/SearchResultBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/SearchResultBlock) 