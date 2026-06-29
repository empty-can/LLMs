

# PassthroughTargetConfiguration
<a name="API_PassthroughTargetConfiguration"></a>

The configuration for an HTTP passthrough target. A passthrough target forwards requests directly to an external HTTP endpoint.

## Contents
<a name="API_PassthroughTargetConfiguration_Contents"></a>

 ** endpoint **   <a name="bedrockagentcorecontrol-Type-PassthroughTargetConfiguration-endpoint"></a>
The HTTPS endpoint that the gateway forwards requests to for this passthrough target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `https://[a-zA-Z0-9\-\.]+(:[0-9]{1,5})?(/.*)?`   
Required: Yes

 ** protocolType **   <a name="bedrockagentcorecontrol-Type-PassthroughTargetConfiguration-protocolType"></a>
The application protocol that the passthrough target implements. This value is required for passthrough targets:  
+  `MCP` - The Model Context Protocol.
+  `A2A` - The Agent-to-Agent protocol.
+  `INFERENCE` - The protocol for routing requests to a large language model (LLM) provider.
+  `CUSTOM` - A custom application protocol.
Type: String  
Valid Values: `MCP | A2A | INFERENCE | CUSTOM`   
Required: Yes

 ** schema **   <a name="bedrockagentcorecontrol-Type-PassthroughTargetConfiguration-schema"></a>
The API schema configuration that defines the structure of the passthrough target's API.  
Type: [HttpApiSchemaConfiguration](API_HttpApiSchemaConfiguration.md) object  
Required: No

 ** stickinessConfiguration **   <a name="bedrockagentcorecontrol-Type-PassthroughTargetConfiguration-stickinessConfiguration"></a>
The session stickiness configuration for the passthrough target. This configuration routes requests within the same session to the same target.  
Type: [StickinessConfiguration](API_StickinessConfiguration.md) object  
Required: No

## See Also
<a name="API_PassthroughTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PassthroughTargetConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PassthroughTargetConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PassthroughTargetConfiguration) 