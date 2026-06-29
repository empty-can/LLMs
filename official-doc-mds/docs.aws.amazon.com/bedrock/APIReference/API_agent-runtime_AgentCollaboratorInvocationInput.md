

# AgentCollaboratorInvocationInput
<a name="API_agent-runtime_AgentCollaboratorInvocationInput"></a>

An agent collaborator invocation input.

## Contents
<a name="API_agent-runtime_AgentCollaboratorInvocationInput_Contents"></a>

 ** agentCollaboratorAliasArn **   <a name="bedrock-Type-agent-runtime_AgentCollaboratorInvocationInput-agentCollaboratorAliasArn"></a>
The collaborator's alias ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}`   
Required: No

 ** agentCollaboratorName **   <a name="bedrock-Type-agent-runtime_AgentCollaboratorInvocationInput-agentCollaboratorName"></a>
The collaborator's name.  
Type: String  
Required: No

 ** input **   <a name="bedrock-Type-agent-runtime_AgentCollaboratorInvocationInput-input"></a>
Text or action invocation result input for the collaborator.  
Type: [AgentCollaboratorInputPayload](API_agent-runtime_AgentCollaboratorInputPayload.md) object  
Required: No

## See Also
<a name="API_agent-runtime_AgentCollaboratorInvocationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgentCollaboratorInvocationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgentCollaboratorInvocationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgentCollaboratorInvocationInput) 