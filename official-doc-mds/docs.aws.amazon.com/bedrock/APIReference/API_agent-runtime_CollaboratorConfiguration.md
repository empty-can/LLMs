

# CollaboratorConfiguration
<a name="API_agent-runtime_CollaboratorConfiguration"></a>

 Settings of an inline collaborator agent. 

## Contents
<a name="API_agent-runtime_CollaboratorConfiguration_Contents"></a>

 ** collaboratorInstruction **   <a name="bedrock-Type-agent-runtime_CollaboratorConfiguration-collaboratorInstruction"></a>
 Instructions that tell the inline collaborator agent what it should do and how it should interact with users.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4000.  
Required: Yes

 ** collaboratorName **   <a name="bedrock-Type-agent-runtime_CollaboratorConfiguration-collaboratorName"></a>
 Name of the inline collaborator agent which must be the same name as specified for `agentName`.   
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** agentAliasArn **   <a name="bedrock-Type-agent-runtime_CollaboratorConfiguration-agentAliasArn"></a>
 The Amazon Resource Name (ARN) of the inline collaborator agent.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}`   
Required: No

 ** relayConversationHistory **   <a name="bedrock-Type-agent-runtime_CollaboratorConfiguration-relayConversationHistory"></a>
 A relay conversation history for the inline collaborator agent.   
Type: String  
Valid Values: `TO_COLLABORATOR | DISABLED`   
Required: No

## See Also
<a name="API_agent-runtime_CollaboratorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/CollaboratorConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/CollaboratorConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/CollaboratorConfiguration) 