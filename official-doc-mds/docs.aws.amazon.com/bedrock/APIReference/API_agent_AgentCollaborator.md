

# AgentCollaborator
<a name="API_agent_AgentCollaborator"></a>

An agent collaborator.

## Contents
<a name="API_agent_AgentCollaborator_Contents"></a>

 ** agentDescriptor **   <a name="bedrock-Type-agent_AgentCollaborator-agentDescriptor"></a>
The collaborator's agent descriptor.  
Type: [AgentDescriptor](API_agent_AgentDescriptor.md) object  
Required: Yes

 ** agentId **   <a name="bedrock-Type-agent_AgentCollaborator-agentId"></a>
The collaborator's agent ID.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** agentVersion **   <a name="bedrock-Type-agent_AgentCollaborator-agentVersion"></a>
The collaborator's agent version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

 ** collaborationInstruction **   <a name="bedrock-Type-agent_AgentCollaborator-collaborationInstruction"></a>
The collaborator's instructions.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4000.  
Required: Yes

 ** collaboratorId **   <a name="bedrock-Type-agent_AgentCollaborator-collaboratorId"></a>
The collaborator's collaborator ID.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** collaboratorName **   <a name="bedrock-Type-agent_AgentCollaborator-collaboratorName"></a>
The collaborator's collaborator name.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_AgentCollaborator-createdAt"></a>
When the collaborator was created.  
Type: Timestamp  
Required: Yes

 ** lastUpdatedAt **   <a name="bedrock-Type-agent_AgentCollaborator-lastUpdatedAt"></a>
When the collaborator was updated.  
Type: Timestamp  
Required: Yes

 ** clientToken **   <a name="bedrock-Type-agent_AgentCollaborator-clientToken"></a>
The collaborator's client token.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** relayConversationHistory **   <a name="bedrock-Type-agent_AgentCollaborator-relayConversationHistory"></a>
The collaborator's relay conversation history.  
Type: String  
Valid Values: `TO_COLLABORATOR | DISABLED`   
Required: No

## See Also
<a name="API_agent_AgentCollaborator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AgentCollaborator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AgentCollaborator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AgentCollaborator) 