

# HarnessAgentCoreMemoryConfiguration
<a name="API_HarnessAgentCoreMemoryConfiguration"></a>

Configuration for AgentCore Memory integration.

## Contents
<a name="API_HarnessAgentCoreMemoryConfiguration_Contents"></a>

 ** arn **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreMemoryConfiguration-arn"></a>
The ARN of the AgentCore Memory resource.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** actorId **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreMemoryConfiguration-actorId"></a>
The actor ID for memory operations.  
Type: String  
Required: No

 ** messagesCount **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreMemoryConfiguration-messagesCount"></a>
The number of messages to retrieve from memory.  
Type: Integer  
Required: No

 ** retrievalConfig **   <a name="bedrockagentcorecontrol-Type-HarnessAgentCoreMemoryConfiguration-retrievalConfig"></a>
The retrieval configuration for long-term memory, mapping namespace path templates to retrieval settings.  
Type: String to [HarnessAgentCoreMemoryRetrievalConfig](API_HarnessAgentCoreMemoryRetrievalConfig.md) object map  
Required: No

## See Also
<a name="API_HarnessAgentCoreMemoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessAgentCoreMemoryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessAgentCoreMemoryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessAgentCoreMemoryConfiguration) 