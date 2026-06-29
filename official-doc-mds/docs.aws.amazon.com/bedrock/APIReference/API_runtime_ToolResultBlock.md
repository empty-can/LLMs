

# ToolResultBlock
<a name="API_runtime_ToolResultBlock"></a>

A tool result block that contains the results for a tool request that the model previously made. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_runtime_ToolResultBlock_Contents"></a>

 ** content **   <a name="bedrock-Type-runtime_ToolResultBlock-content"></a>
The content for tool result content block.  
Type: Array of [ToolResultContentBlock](API_runtime_ToolResultContentBlock.md) objects  
Required: Yes

 ** toolUseId **   <a name="bedrock-Type-runtime_ToolResultBlock-toolUseId"></a>
The ID of the tool request that this is the result for.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** status **   <a name="bedrock-Type-runtime_ToolResultBlock-status"></a>
The status for the tool result content block.  
This field is only supported by Amazon Nova and Anthropic Claude 3 and 4 models.
Type: String  
Valid Values: `success | error`   
Required: No

 ** type **   <a name="bedrock-Type-runtime_ToolResultBlock-type"></a>
The type for the tool result content block.  
Type: String  
Required: No

## See Also
<a name="API_runtime_ToolResultBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ToolResultBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ToolResultBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ToolResultBlock) 