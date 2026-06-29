

# AgentAlias
<a name="API_agent_AgentAlias"></a>

Contains details about an alias of an agent.

## Contents
<a name="API_agent_AgentAlias_Contents"></a>

 ** agentAliasArn **   <a name="bedrock-Type-agent_AgentAlias-agentAliasArn"></a>
The Amazon Resource Name (ARN) of the alias of the agent.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}`   
Required: Yes

 ** agentAliasId **   <a name="bedrock-Type-agent_AgentAlias-agentAliasId"></a>
The unique identifier of the alias of the agent.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `(\bTSTALIASID\b|[0-9a-zA-Z]+)`   
Required: Yes

 ** agentAliasName **   <a name="bedrock-Type-agent_AgentAlias-agentAliasName"></a>
The name of the alias of the agent.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** agentAliasStatus **   <a name="bedrock-Type-agent_AgentAlias-agentAliasStatus"></a>
The status of the alias of the agent and whether it is ready for use. The following statuses are possible:  
+ CREATING – The agent alias is being created.
+ PREPARED – The agent alias is finished being created or updated and is ready to be invoked.
+ FAILED – The agent alias API operation failed.
+ UPDATING – The agent alias is being updated.
+ DELETING – The agent alias is being deleted.
+ DISSOCIATED - The agent alias has no version associated with it.
Type: String  
Valid Values: `CREATING | PREPARED | FAILED | UPDATING | DELETING | DISSOCIATED`   
Required: Yes

 ** agentId **   <a name="bedrock-Type-agent_AgentAlias-agentId"></a>
The unique identifier of the agent.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_AgentAlias-createdAt"></a>
The time at which the alias of the agent was created.  
Type: Timestamp  
Required: Yes

 ** routingConfiguration **   <a name="bedrock-Type-agent_AgentAlias-routingConfiguration"></a>
Contains details about the routing configuration of the alias.  
Type: Array of [AgentAliasRoutingConfigurationListItem](API_agent_AgentAliasRoutingConfigurationListItem.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_AgentAlias-updatedAt"></a>
The time at which the alias was last updated.  
Type: Timestamp  
Required: Yes

 ** agentAliasHistoryEvents **   <a name="bedrock-Type-agent_AgentAlias-agentAliasHistoryEvents"></a>
Contains details about the history of the alias.  
Type: Array of [AgentAliasHistoryEvent](API_agent_AgentAliasHistoryEvent.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** aliasInvocationState **   <a name="bedrock-Type-agent_AgentAlias-aliasInvocationState"></a>
The invocation state for the agent alias. If the agent alias is running, the value is `ACCEPT_INVOCATIONS`. If the agent alias is paused, the value is `REJECT_INVOCATIONS`. Use the `UpdateAgentAlias` operation to change the invocation state.  
Type: String  
Valid Values: `ACCEPT_INVOCATIONS | REJECT_INVOCATIONS`   
Required: No

 ** clientToken **   <a name="bedrock-Type-agent_AgentAlias-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** description **   <a name="bedrock-Type-agent_AgentAlias-description"></a>
The description of the alias of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** failureReasons **   <a name="bedrock-Type-agent_AgentAlias-failureReasons"></a>
Information on the failure of Provisioned Throughput assigned to an agent alias.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2048 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: No

## See Also
<a name="API_agent_AgentAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentAlias) 