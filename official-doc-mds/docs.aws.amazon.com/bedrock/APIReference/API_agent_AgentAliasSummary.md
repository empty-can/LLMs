

# AgentAliasSummary
<a name="API_agent_AgentAliasSummary"></a>

Contains details about an alias of an agent.

## Contents
<a name="API_agent_AgentAliasSummary_Contents"></a>

 ** agentAliasId **   <a name="bedrock-Type-agent_AgentAliasSummary-agentAliasId"></a>
Contains details about   
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** agentAliasName **   <a name="bedrock-Type-agent_AgentAliasSummary-agentAliasName"></a>
The name of the alias.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** agentAliasStatus **   <a name="bedrock-Type-agent_AgentAliasSummary-agentAliasStatus"></a>
The status of the alias.  
Type: String  
Valid Values: `CREATING | PREPARED | FAILED | UPDATING | DELETING | DISSOCIATED`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_AgentAliasSummary-createdAt"></a>
The time at which the alias of the agent was created.  
Type: Timestamp  
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_AgentAliasSummary-updatedAt"></a>
The time at which the alias was last updated.  
Type: Timestamp  
Required: Yes

 ** aliasInvocationState **   <a name="bedrock-Type-agent_AgentAliasSummary-aliasInvocationState"></a>
The invocation state for the agent alias. If the agent alias is running, the value is `ACCEPT_INVOCATIONS`. If the agent alias is paused, the value is `REJECT_INVOCATIONS`. Use the `UpdateAgentAlias` operation to change the invocation state.  
Type: String  
Valid Values: `ACCEPT_INVOCATIONS | REJECT_INVOCATIONS`   
Required: No

 ** description **   <a name="bedrock-Type-agent_AgentAliasSummary-description"></a>
The description of the alias.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** routingConfiguration **   <a name="bedrock-Type-agent_AgentAliasSummary-routingConfiguration"></a>
Contains details about the version of the agent with which the alias is associated.  
Type: Array of [AgentAliasRoutingConfigurationListItem](API_agent_AgentAliasRoutingConfigurationListItem.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

## See Also
<a name="API_agent_AgentAliasSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentAliasSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentAliasSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentAliasSummary) 