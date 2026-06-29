

# InvocationInput
<a name="API_agent-runtime_InvocationInput"></a>

Contains information pertaining to the action group or knowledge base that is being invoked.

## Contents
<a name="API_agent-runtime_InvocationInput_Contents"></a>

 ** actionGroupInvocationInput **   <a name="bedrock-Type-agent-runtime_InvocationInput-actionGroupInvocationInput"></a>
Contains information about the action group to be invoked.  
Type: [ActionGroupInvocationInput](API_agent-runtime_ActionGroupInvocationInput.md) object  
Required: No

 ** agentCollaboratorInvocationInput **   <a name="bedrock-Type-agent-runtime_InvocationInput-agentCollaboratorInvocationInput"></a>
The collaborator's invocation input.  
Type: [AgentCollaboratorInvocationInput](API_agent-runtime_AgentCollaboratorInvocationInput.md) object  
Required: No

 ** codeInterpreterInvocationInput **   <a name="bedrock-Type-agent-runtime_InvocationInput-codeInterpreterInvocationInput"></a>
Contains information about the code interpreter to be invoked.  
Type: [CodeInterpreterInvocationInput](API_agent-runtime_CodeInterpreterInvocationInput.md) object  
Required: No

 ** invocationType **   <a name="bedrock-Type-agent-runtime_InvocationInput-invocationType"></a>
Specifies whether the agent is invoking an action group or a knowledge base.  
Type: String  
Valid Values: `ACTION_GROUP | KNOWLEDGE_BASE | FINISH | ACTION_GROUP_CODE_INTERPRETER | AGENT_COLLABORATOR`   
Required: No

 ** knowledgeBaseLookupInput **   <a name="bedrock-Type-agent-runtime_InvocationInput-knowledgeBaseLookupInput"></a>
Contains details about the knowledge base to look up and the query to be made.  
Type: [KnowledgeBaseLookupInput](API_agent-runtime_KnowledgeBaseLookupInput.md) object  
Required: No

 ** traceId **   <a name="bedrock-Type-agent-runtime_InvocationInput-traceId"></a>
The unique identifier of the trace.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 16.  
Required: No

## See Also
<a name="API_agent-runtime_InvocationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/InvocationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/InvocationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/InvocationInput) 