

# ToolUseBlock
<a name="API_runtime_ToolUseBlock"></a>

A tool use content block. Contains information about a tool that the model is requesting be run., The model uses the result from the tool to generate a response. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_runtime_ToolUseBlock_Contents"></a>

 ** input **   <a name="bedrock-Type-runtime_ToolUseBlock-input"></a>
The input to pass to the tool.   
Type: JSON value  
Required: Yes

 ** name **   <a name="bedrock-Type-runtime_ToolUseBlock-name"></a>
The name of the tool that the model wants to use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** toolUseId **   <a name="bedrock-Type-runtime_ToolUseBlock-toolUseId"></a>
The ID for the tool request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** type **   <a name="bedrock-Type-runtime_ToolUseBlock-type"></a>
The type for the tool request.  
Type: String  
Valid Values: `server_tool_use`   
Required: No

## See Also
<a name="API_runtime_ToolUseBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ToolUseBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ToolUseBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ToolUseBlock) 