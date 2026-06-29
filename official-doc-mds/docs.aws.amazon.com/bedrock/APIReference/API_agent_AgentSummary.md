

# AgentSummary
<a name="API_agent_AgentSummary"></a>

Contains details about an agent.

## Contents
<a name="API_agent_AgentSummary_Contents"></a>

 ** agentId **   <a name="bedrock-Type-agent_AgentSummary-agentId"></a>
The unique identifier of the agent.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** agentName **   <a name="bedrock-Type-agent_AgentSummary-agentName"></a>
The name of the agent.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** agentStatus **   <a name="bedrock-Type-agent_AgentSummary-agentStatus"></a>
The status of the agent.  
Type: String  
Valid Values: `CREATING | PREPARING | PREPARED | NOT_PREPARED | DELETING | FAILED | VERSIONING | UPDATING`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_AgentSummary-updatedAt"></a>
The time at which the agent was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrock-Type-agent_AgentSummary-description"></a>
The description of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** guardrailConfiguration **   <a name="bedrock-Type-agent_AgentSummary-guardrailConfiguration"></a>
Details about the guardrail associated with the agent.  
Type: [GuardrailConfiguration](API_agent_GuardrailConfiguration.md) object  
Required: No

 ** latestAgentVersion **   <a name="bedrock-Type-agent_AgentSummary-latestAgentVersion"></a>
The latest version of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: No

## See Also
<a name="API_agent_AgentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentSummary) 