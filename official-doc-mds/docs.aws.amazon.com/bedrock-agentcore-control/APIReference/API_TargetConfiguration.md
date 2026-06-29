

# TargetConfiguration
<a name="API_TargetConfiguration"></a>

The configuration for a gateway target. This structure defines how the gateway connects to and interacts with the target endpoint.

## Contents
<a name="API_TargetConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** http **   <a name="bedrockagentcorecontrol-Type-TargetConfiguration-http"></a>
The HTTP target configuration. Use this to route gateway requests to an HTTP-based endpoint such as an AgentCore Runtime.  
Type: [HttpTargetConfiguration](API_HttpTargetConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** inference **   <a name="bedrockagentcorecontrol-Type-TargetConfiguration-inference"></a>
The inference configuration for the target. This configuration routes requests to a large language model (LLM) provider.  
Type: [InferenceTargetConfiguration](API_InferenceTargetConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** mcp **   <a name="bedrockagentcorecontrol-Type-TargetConfiguration-mcp"></a>
The Model Context Protocol (MCP) configuration for the target. This configuration defines how the gateway uses MCP to communicate with the target.  
Type: [McpTargetConfiguration](API_McpTargetConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_TargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/TargetConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/TargetConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/TargetConfiguration) 