

# AgentAliasRoutingConfigurationListItem
<a name="API_agent_AgentAliasRoutingConfigurationListItem"></a>

Contains details about the routing configuration of the alias.

## Contents
<a name="API_agent_AgentAliasRoutingConfigurationListItem_Contents"></a>

 ** agentVersion **   <a name="bedrock-Type-agent_AgentAliasRoutingConfigurationListItem-agentVersion"></a>
The version of the agent with which the alias is associated.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: No

 ** provisionedThroughput **   <a name="bedrock-Type-agent_AgentAliasRoutingConfigurationListItem-provisionedThroughput"></a>
Information on the Provisioned Throughput assigned to an agent alias.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `((([0-9a-zA-Z][_-]?){1,63})|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:provisioned-model/[a-z0-9]{12}))`   
Required: No

## See Also
<a name="API_agent_AgentAliasRoutingConfigurationListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentAliasRoutingConfigurationListItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentAliasRoutingConfigurationListItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentAliasRoutingConfigurationListItem) 