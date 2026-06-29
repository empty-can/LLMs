

# AgentKnowledgeBase
<a name="API_agent_AgentKnowledgeBase"></a>

Contains details about a knowledge base that is associated with an agent.

## Contents
<a name="API_agent_AgentKnowledgeBase_Contents"></a>

 ** agentId **   <a name="bedrock-Type-agent_AgentKnowledgeBase-agentId"></a>
The unique identifier of the agent with which the knowledge base is associated.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** agentVersion **   <a name="bedrock-Type-agent_AgentKnowledgeBase-agentVersion"></a>
The version of the agent with which the knowledge base is associated.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_AgentKnowledgeBase-createdAt"></a>
The time at which the association between the agent and the knowledge base was created.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrock-Type-agent_AgentKnowledgeBase-description"></a>
The description of the association between the agent and the knowledge base.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: Yes

 ** knowledgeBaseId **   <a name="bedrock-Type-agent_AgentKnowledgeBase-knowledgeBaseId"></a>
The unique identifier of the association between the agent and the knowledge base.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** knowledgeBaseState **   <a name="bedrock-Type-agent_AgentKnowledgeBase-knowledgeBaseState"></a>
Specifies whether to use the knowledge base or not when sending an [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) request.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_AgentKnowledgeBase-updatedAt"></a>
The time at which the association between the agent and the knowledge base was last updated.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_agent_AgentKnowledgeBase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentKnowledgeBase) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentKnowledgeBase) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentKnowledgeBase) 