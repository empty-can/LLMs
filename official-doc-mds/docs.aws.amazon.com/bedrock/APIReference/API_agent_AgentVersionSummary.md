

# AgentVersionSummary
<a name="API_agent_AgentVersionSummary"></a>

Contains details about a version of an agent.

## Contents
<a name="API_agent_AgentVersionSummary_Contents"></a>

 ** agentName **   <a name="bedrock-Type-agent_AgentVersionSummary-agentName"></a>
The name of the agent to which the version belongs.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** agentStatus **   <a name="bedrock-Type-agent_AgentVersionSummary-agentStatus"></a>
The status of the agent to which the version belongs.  
Type: String  
Valid Values: `CREATING | PREPARING | PREPARED | NOT_PREPARED | DELETING | FAILED | VERSIONING | UPDATING`   
Required: Yes

 ** agentVersion **   <a name="bedrock-Type-agent_AgentVersionSummary-agentVersion"></a>
The version of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_AgentVersionSummary-createdAt"></a>
The time at which the version was created.  
Type: Timestamp  
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_AgentVersionSummary-updatedAt"></a>
The time at which the version was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrock-Type-agent_AgentVersionSummary-description"></a>
The description of the version of the agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** guardrailConfiguration **   <a name="bedrock-Type-agent_AgentVersionSummary-guardrailConfiguration"></a>
Details about the guardrail associated with the agent.  
Type: [GuardrailConfiguration](API_agent_GuardrailConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_AgentVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentVersionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentVersionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentVersionSummary) 