

# ToolUseBlockStart
<a name="API_runtime_ToolUseBlockStart"></a>

The start of a tool use block. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide.

## Contents
<a name="API_runtime_ToolUseBlockStart_Contents"></a>

 ** name **   <a name="bedrock-Type-runtime_ToolUseBlockStart-name"></a>
The name of the tool that the model is requesting to use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** toolUseId **   <a name="bedrock-Type-runtime_ToolUseBlockStart-toolUseId"></a>
The ID for the tool request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** type **   <a name="bedrock-Type-runtime_ToolUseBlockStart-type"></a>
The type for the tool request.  
Type: String  
Valid Values: `server_tool_use`   
Required: No

## See Also
<a name="API_runtime_ToolUseBlockStart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ToolUseBlockStart) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ToolUseBlockStart) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ToolUseBlockStart) 