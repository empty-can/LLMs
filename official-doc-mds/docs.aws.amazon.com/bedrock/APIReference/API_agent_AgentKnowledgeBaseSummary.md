

# AgentKnowledgeBaseSummary
<a name="API_agent_AgentKnowledgeBaseSummary"></a>

Contains details about a knowledge base associated with an agent.

## Contents
<a name="API_agent_AgentKnowledgeBaseSummary_Contents"></a>

 ** knowledgeBaseId **   <a name="bedrock-Type-agent_AgentKnowledgeBaseSummary-knowledgeBaseId"></a>
The unique identifier of the knowledge base associated with an agent.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** knowledgeBaseState **   <a name="bedrock-Type-agent_AgentKnowledgeBaseSummary-knowledgeBaseState"></a>
Specifies whether the agent uses the knowledge base or not when sending an [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) request.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_AgentKnowledgeBaseSummary-updatedAt"></a>
The time at which the knowledge base associated with an agent was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrock-Type-agent_AgentKnowledgeBaseSummary-description"></a>
The description of the knowledge base associated with an agent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

## See Also
<a name="API_agent_AgentKnowledgeBaseSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentKnowledgeBaseSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentKnowledgeBaseSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentKnowledgeBaseSummary) 