

# AgentAliasHistoryEvent
<a name="API_agent_AgentAliasHistoryEvent"></a>

Contains details about the history of the alias.

## Contents
<a name="API_agent_AgentAliasHistoryEvent_Contents"></a>

 ** endDate **   <a name="bedrock-Type-agent_AgentAliasHistoryEvent-endDate"></a>
The date that the alias stopped being associated to the version in the `routingConfiguration` object  
Type: Timestamp  
Required: No

 ** routingConfiguration **   <a name="bedrock-Type-agent_AgentAliasHistoryEvent-routingConfiguration"></a>
Contains details about the version of the agent with which the alias is associated.  
Type: Array of [AgentAliasRoutingConfigurationListItem](API_agent_AgentAliasRoutingConfigurationListItem.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

 ** startDate **   <a name="bedrock-Type-agent_AgentAliasHistoryEvent-startDate"></a>
The date that the alias began being associated to the version in the `routingConfiguration` object.  
Type: Timestamp  
Required: No

## See Also
<a name="API_agent_AgentAliasHistoryEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentAliasHistoryEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentAliasHistoryEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentAliasHistoryEvent) 