

# AgentCollaboratorOutputPayload
<a name="API_agent-runtime_AgentCollaboratorOutputPayload"></a>

Output from an agent collaborator. The output can be text or an action invocation result.

## Contents
<a name="API_agent-runtime_AgentCollaboratorOutputPayload_Contents"></a>

 ** returnControlPayload **   <a name="bedrock-Type-agent-runtime_AgentCollaboratorOutputPayload-returnControlPayload"></a>
An action invocation result.  
Type: [ReturnControlPayload](API_agent-runtime_ReturnControlPayload.md) object  
Required: No

 ** text **   <a name="bedrock-Type-agent-runtime_AgentCollaboratorOutputPayload-text"></a>
Text output.  
Type: String  
Required: No

 ** type **   <a name="bedrock-Type-agent-runtime_AgentCollaboratorOutputPayload-type"></a>
The type of output.  
Type: String  
Valid Values: `TEXT | RETURN_CONTROL`   
Required: No

## See Also
<a name="API_agent-runtime_AgentCollaboratorOutputPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgentCollaboratorOutputPayload) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgentCollaboratorOutputPayload) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgentCollaboratorOutputPayload) 