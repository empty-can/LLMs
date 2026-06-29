

# ToolResultContentBlock
<a name="API_runtime_ToolResultContentBlock"></a>

The tool result content block. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_runtime_ToolResultContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** document **   <a name="bedrock-Type-runtime_ToolResultContentBlock-document"></a>
A tool result that is a document.  
Type: [DocumentBlock](API_runtime_DocumentBlock.md) object  
Required: No

 ** image **   <a name="bedrock-Type-runtime_ToolResultContentBlock-image"></a>
A tool result that is an image.   
This field is only supported by Amazon Nova and Anthropic Claude 3 and 4 models.
Type: [ImageBlock](API_runtime_ImageBlock.md) object  
Required: No

 ** json **   <a name="bedrock-Type-runtime_ToolResultContentBlock-json"></a>
A tool result that is JSON format data.   
Type: JSON value  
Required: No

 ** searchResult **   <a name="bedrock-Type-runtime_ToolResultContentBlock-searchResult"></a>
A tool result that is a search result.  
Type: [SearchResultBlock](API_runtime_SearchResultBlock.md) object  
Required: No

 ** text **   <a name="bedrock-Type-runtime_ToolResultContentBlock-text"></a>
A tool result that is text.   
Type: String  
Required: No

 ** video **   <a name="bedrock-Type-runtime_ToolResultContentBlock-video"></a>
A tool result that is video.  
Type: [VideoBlock](API_runtime_VideoBlock.md) object  
Required: No

## See Also
<a name="API_runtime_ToolResultContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ToolResultContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ToolResultContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ToolResultContentBlock) 