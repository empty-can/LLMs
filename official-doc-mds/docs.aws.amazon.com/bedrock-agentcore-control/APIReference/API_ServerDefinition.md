

# ServerDefinition
<a name="API_ServerDefinition"></a>

The server definition for an MCP descriptor. Contains the schema version and inline content for the MCP server configuration.

## Contents
<a name="API_ServerDefinition_Contents"></a>

 ** inlineContent **   <a name="bedrockagentcorecontrol-Type-ServerDefinition-inlineContent"></a>
The JSON content containing the MCP server definition, conforming to the MCP protocol specification.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** schemaVersion **   <a name="bedrockagentcorecontrol-Type-ServerDefinition-schemaVersion"></a>
The schema version of the server definition based on the MCP protocol specification. If not specified, the version is auto-detected from the content.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

## See Also
<a name="API_ServerDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ServerDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ServerDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ServerDefinition) 