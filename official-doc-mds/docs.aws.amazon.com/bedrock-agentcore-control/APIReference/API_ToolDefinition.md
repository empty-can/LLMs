

# ToolDefinition
<a name="API_ToolDefinition"></a>

A tool definition for a gateway target. This structure defines a tool that the target exposes through the Model Context Protocol.

## Contents
<a name="API_ToolDefinition_Contents"></a>

 ** description **   <a name="bedrockagentcorecontrol-Type-ToolDefinition-description"></a>
The description of the tool. This description provides information about the purpose and usage of the tool.  
Type: String  
Required: Yes

 ** inputSchema **   <a name="bedrockagentcorecontrol-Type-ToolDefinition-inputSchema"></a>
The input schema for the tool. This schema defines the structure of the input that the tool accepts.  
Type: [SchemaDefinition](API_SchemaDefinition.md) object  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-ToolDefinition-name"></a>
The name of the tool. This name identifies the tool in the Model Context Protocol.  
Type: String  
Required: Yes

 ** outputSchema **   <a name="bedrockagentcorecontrol-Type-ToolDefinition-outputSchema"></a>
The output schema for the tool. This schema defines the structure of the output that the tool produces.  
Type: [SchemaDefinition](API_SchemaDefinition.md) object  
Required: No

## See Also
<a name="API_ToolDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ToolDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ToolDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ToolDefinition) 