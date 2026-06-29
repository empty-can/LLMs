

# ContentBlock
<a name="API_ContentBlock"></a>

A block of content in a response.

## Contents
<a name="API_ContentBlock_Contents"></a>

 ** type **   <a name="BedrockAgentCore-Type-ContentBlock-type"></a>
The type of content in the block.  
Type: String  
Valid Values: `text | image | resource | resource_link`   
Required: Yes

 ** data **   <a name="BedrockAgentCore-Type-ContentBlock-data"></a>
The binary data content of the block.  
Type: Base64-encoded binary data object  
Required: No

 ** description **   <a name="BedrockAgentCore-Type-ContentBlock-description"></a>
The description of the content block.  
Type: String  
Required: No

 ** mimeType **   <a name="BedrockAgentCore-Type-ContentBlock-mimeType"></a>
The MIME type of the content.  
Type: String  
Required: No

 ** name **   <a name="BedrockAgentCore-Type-ContentBlock-name"></a>
The name of the content block.  
Type: String  
Required: No

 ** resource **   <a name="BedrockAgentCore-Type-ContentBlock-resource"></a>
The resource associated with the content block.  
Type: [ResourceContent](API_ResourceContent.md) object  
Required: No

 ** size **   <a name="BedrockAgentCore-Type-ContentBlock-size"></a>
The size of the content in bytes.  
Type: Long  
Required: No

 ** text **   <a name="BedrockAgentCore-Type-ContentBlock-text"></a>
The text content of the block.  
Type: String  
Required: No

 ** uri **   <a name="BedrockAgentCore-Type-ContentBlock-uri"></a>
The URI of the content.  
Type: String  
Required: No

## See Also
<a name="API_ContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ContentBlock) 