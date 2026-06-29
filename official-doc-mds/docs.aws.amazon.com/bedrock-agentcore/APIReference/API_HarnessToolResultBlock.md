

# HarnessToolResultBlock
<a name="API_HarnessToolResultBlock"></a>

The result of a tool execution.

## Contents
<a name="API_HarnessToolResultBlock_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-HarnessToolResultBlock-content"></a>
The content of the tool result.  
Type: Array of [HarnessToolResultContentBlock](API_HarnessToolResultContentBlock.md) objects  
Required: Yes

 ** toolUseId **   <a name="BedrockAgentCore-Type-HarnessToolResultBlock-toolUseId"></a>
The tool use ID that this result corresponds to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-HarnessToolResultBlock-status"></a>
The status of the tool execution.  
Type: String  
Valid Values: `success | error`   
Required: No

 ** type **   <a name="BedrockAgentCore-Type-HarnessToolResultBlock-type"></a>
The type of tool use that produced this result.  
Type: String  
Valid Values: `tool_use | server_tool_use | mcp_tool_use`   
Required: No

## See Also
<a name="API_HarnessToolResultBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolResultBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolResultBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolResultBlock) 