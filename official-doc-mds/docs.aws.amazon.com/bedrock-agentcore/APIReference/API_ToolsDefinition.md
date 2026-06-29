

# ToolsDefinition
<a name="API_ToolsDefinition"></a>

 The MCP tools definition with a protocol version and inline content. The `protocolVersion` identifies the MCP protocol version that the tools conform to. This differs from `schemaVersion` in the server definition, which identifies the server configuration schema format.

## Contents
<a name="API_ToolsDefinition_Contents"></a>

 ** inlineContent **   <a name="BedrockAgentCore-Type-ToolsDefinition-inlineContent"></a>
 The inline content of the tools definition.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 409600.  
Required: No

 ** protocolVersion **   <a name="BedrockAgentCore-Type-ToolsDefinition-protocolVersion"></a>
 The MCP protocol version that the tools conform to. This differs from the `schemaVersion` field in the server definition, which identifies the server configuration schema format.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

## See Also
<a name="API_ToolsDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolsDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolsDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolsDefinition) 