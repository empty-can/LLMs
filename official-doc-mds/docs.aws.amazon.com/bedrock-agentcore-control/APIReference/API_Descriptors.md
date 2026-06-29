

# Descriptors
<a name="API_Descriptors"></a>

Contains descriptor-type-specific configurations for a registry record. Only the descriptor matching the record's `descriptorType` should be populated.

## Contents
<a name="API_Descriptors_Contents"></a>

 ** a2a **   <a name="bedrockagentcorecontrol-Type-Descriptors-a2a"></a>
The Agent-to-Agent (A2A) protocol descriptor configuration. Use this when the `descriptorType` is `A2A`.  
Type: [A2aDescriptor](API_A2aDescriptor.md) object  
Required: No

 ** agentSkills **   <a name="bedrockagentcorecontrol-Type-Descriptors-agentSkills"></a>
The agent skills descriptor configuration. Use this when the `descriptorType` is `AGENT_SKILLS`.  
Type: [AgentSkillsDescriptor](API_AgentSkillsDescriptor.md) object  
Required: No

 ** custom **   <a name="bedrockagentcorecontrol-Type-Descriptors-custom"></a>
The custom descriptor configuration. Use this when the `descriptorType` is `CUSTOM`.  
Type: [CustomDescriptor](API_CustomDescriptor.md) object  
Required: No

 ** mcp **   <a name="bedrockagentcorecontrol-Type-Descriptors-mcp"></a>
The Model Context Protocol (MCP) descriptor configuration. Use this when the `descriptorType` is `MCP`.  
Type: [McpDescriptor](API_McpDescriptor.md) object  
Required: No

## See Also
<a name="API_Descriptors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Descriptors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Descriptors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Descriptors) 