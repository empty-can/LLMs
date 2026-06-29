

# HarnessToolUseBlock
<a name="API_HarnessToolUseBlock"></a>

A tool use request from the model.

## Contents
<a name="API_HarnessToolUseBlock_Contents"></a>

 ** input **   <a name="BedrockAgentCore-Type-HarnessToolUseBlock-input"></a>
The JSON input to pass to the tool.  
Type: JSON value  
Required: Yes

 ** name **   <a name="BedrockAgentCore-Type-HarnessToolUseBlock-name"></a>
The name of the tool to call.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** toolUseId **   <a name="BedrockAgentCore-Type-HarnessToolUseBlock-toolUseId"></a>
The unique ID of this tool use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** serverName **   <a name="BedrockAgentCore-Type-HarnessToolUseBlock-serverName"></a>
The name of the MCP server providing this tool.  
Type: String  
Required: No

 ** type **   <a name="BedrockAgentCore-Type-HarnessToolUseBlock-type"></a>
The type of tool use.  
Type: String  
Valid Values: `tool_use | server_tool_use | mcp_tool_use`   
Required: No

## See Also
<a name="API_HarnessToolUseBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolUseBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolUseBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolUseBlock) 