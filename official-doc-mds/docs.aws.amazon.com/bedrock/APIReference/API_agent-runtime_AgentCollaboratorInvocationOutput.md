

# AgentCollaboratorInvocationOutput
<a name="API_agent-runtime_AgentCollaboratorInvocationOutput"></a>

Output from an agent collaborator.

## Contents
<a name="API_agent-runtime_AgentCollaboratorInvocationOutput_Contents"></a>

 ** agentCollaboratorAliasArn **   <a name="bedrock-Type-agent-runtime_AgentCollaboratorInvocationOutput-agentCollaboratorAliasArn"></a>
The output's agent collaborator alias ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}`   
Required: No

 ** agentCollaboratorName **   <a name="bedrock-Type-agent-runtime_AgentCollaboratorInvocationOutput-agentCollaboratorName"></a>
The output's agent collaborator name.  
Type: String  
Required: No

 ** metadata **   <a name="bedrock-Type-agent-runtime_AgentCollaboratorInvocationOutput-metadata"></a>
Contains information about the output from the agent collaborator.  
Type: [Metadata](API_agent-runtime_Metadata.md) object  
Required: No

 ** output **   <a name="bedrock-Type-agent-runtime_AgentCollaboratorInvocationOutput-output"></a>
The output's output.  
Type: [AgentCollaboratorOutputPayload](API_agent-runtime_AgentCollaboratorOutputPayload.md) object  
Required: No

## See Also
<a name="API_agent-runtime_AgentCollaboratorInvocationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgentCollaboratorInvocationOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgentCollaboratorInvocationOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgentCollaboratorInvocationOutput) 