

# ToolResultBlockStart
<a name="API_runtime_ToolResultBlockStart"></a>

The start of a tool result block. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_runtime_ToolResultBlockStart_Contents"></a>

 ** toolUseId **   <a name="bedrock-Type-runtime_ToolResultBlockStart-toolUseId"></a>
The ID of the tool that was used to generate this tool result block.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** status **   <a name="bedrock-Type-runtime_ToolResultBlockStart-status"></a>
The status of the tool result block.  
Type: String  
Valid Values: `success | error`   
Required: No

 ** type **   <a name="bedrock-Type-runtime_ToolResultBlockStart-type"></a>
The type for the tool that was used to generate this tool result block.  
Type: String  
Required: No

## See Also
<a name="API_runtime_ToolResultBlockStart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ToolResultBlockStart) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ToolResultBlockStart) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ToolResultBlockStart) 