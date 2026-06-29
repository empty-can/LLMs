

# Descriptors
<a name="API_Descriptors"></a>

 Contains the descriptor configuration for a registry record. Only the field that matches the record's `descriptorType` is populated.

## Contents
<a name="API_Descriptors_Contents"></a>

 ** a2a **   <a name="BedrockAgentCore-Type-Descriptors-a2a"></a>
 The A2A (Agent-to-Agent) descriptor configuration. Populated when the record's `descriptorType` is `A2A`.  
Type: [A2aDescriptor](API_A2aDescriptor.md) object  
Required: No

 ** agentSkills **   <a name="BedrockAgentCore-Type-Descriptors-agentSkills"></a>
 The agent skills descriptor configuration. Populated when the record's `descriptorType` is `AGENT_SKILLS`.  
Type: [AgentSkillsDescriptor](API_AgentSkillsDescriptor.md) object  
Required: No

 ** custom **   <a name="BedrockAgentCore-Type-Descriptors-custom"></a>
 The custom descriptor configuration. Populated when the record's `descriptorType` is `CUSTOM`.  
Type: [CustomDescriptor](API_CustomDescriptor.md) object  
Required: No

 ** mcp **   <a name="BedrockAgentCore-Type-Descriptors-mcp"></a>
 The MCP (Model Context Protocol) descriptor configuration. Populated when the record's `descriptorType` is `MCP`.  
Type: [McpDescriptor](API_McpDescriptor.md) object  
Required: No

## See Also
<a name="API_Descriptors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Descriptors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Descriptors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Descriptors) 