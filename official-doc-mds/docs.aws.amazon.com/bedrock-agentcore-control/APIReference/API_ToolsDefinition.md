

# ToolsDefinition
<a name="API_ToolsDefinition"></a>

The tools definition for an MCP descriptor. Contains the protocol version and inline content describing the available tools.

## Contents
<a name="API_ToolsDefinition_Contents"></a>

 ** inlineContent **   <a name="bedrockagentcorecontrol-Type-ToolsDefinition-inlineContent"></a>
The JSON content containing the MCP tools definition, conforming to the MCP protocol specification.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** protocolVersion **   <a name="bedrockagentcorecontrol-Type-ToolsDefinition-protocolVersion"></a>
The protocol version of the tools definition based on the MCP protocol specification. If not specified, the version is auto-detected from the content.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

## See Also
<a name="API_ToolsDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ToolsDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ToolsDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ToolsDefinition) 