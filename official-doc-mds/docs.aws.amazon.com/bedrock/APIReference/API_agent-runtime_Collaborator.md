

# Collaborator
<a name="API_agent-runtime_Collaborator"></a>

 List of inline collaborators. 

## Contents
<a name="API_agent-runtime_Collaborator_Contents"></a>

 ** foundationModel **   <a name="bedrock-Type-agent-runtime_Collaborator-foundationModel"></a>
 The foundation model used by the inline collaborator agent.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `.*(^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2})))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+))$|(^arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{1,20}):(|[0-9]{12}):inference-profile/[a-zA-Z0-9-:.]+)`   
Required: Yes

 ** instruction **   <a name="bedrock-Type-agent-runtime_Collaborator-instruction"></a>
 Instruction that tell the inline collaborator agent what it should do and how it should interact with users.   
Type: String  
Length Constraints: Minimum length of 40.  
Required: Yes

 ** actionGroups **   <a name="bedrock-Type-agent-runtime_Collaborator-actionGroups"></a>
 List of action groups with each action group defining tasks the inline collaborator agent needs to carry out.   
Type: Array of [AgentActionGroup](API_agent-runtime_AgentActionGroup.md) objects  
Required: No

 ** agentCollaboration **   <a name="bedrock-Type-agent-runtime_Collaborator-agentCollaboration"></a>
 Defines how the inline supervisor agent handles information across multiple collaborator agents to coordinate a final response.   
Type: String  
Valid Values: `SUPERVISOR | SUPERVISOR_ROUTER | DISABLED`   
Required: No

 ** agentName **   <a name="bedrock-Type-agent-runtime_Collaborator-agentName"></a>
 Name of the inline collaborator agent which must be the same name as specified for `collaboratorName`.   
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: No

 ** collaboratorConfigurations **   <a name="bedrock-Type-agent-runtime_Collaborator-collaboratorConfigurations"></a>
 Settings of the collaborator agent.   
Type: Array of [CollaboratorConfiguration](API_agent-runtime_CollaboratorConfiguration.md) objects  
Required: No

 ** customerEncryptionKeyArn **   <a name="bedrock-Type-agent-runtime_Collaborator-customerEncryptionKeyArn"></a>
 The Amazon Resource Name (ARN) of the AWS KMS key that encrypts the inline collaborator.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** guardrailConfiguration **   <a name="bedrock-Type-agent-runtime_Collaborator-guardrailConfiguration"></a>
 Details of the guardwrail associated with the inline collaborator.   
Type: [GuardrailConfigurationWithArn](API_agent-runtime_GuardrailConfigurationWithArn.md) object  
Required: No

 ** idleSessionTTLInSeconds **   <a name="bedrock-Type-agent-runtime_Collaborator-idleSessionTTLInSeconds"></a>
 The number of seconds for which the Amazon Bedrock keeps information about the user's conversation with the inline collaborator agent.  
A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.   
Type: Integer  
Valid Range: Minimum value of 60. Maximum value of 3600.  
Required: No

 ** knowledgeBases **   <a name="bedrock-Type-agent-runtime_Collaborator-knowledgeBases"></a>
 Knowledge base associated with the inline collaborator agent.   
Type: Array of [KnowledgeBase](API_agent-runtime_KnowledgeBase.md) objects  
Required: No

 ** promptOverrideConfiguration **   <a name="bedrock-Type-agent-runtime_Collaborator-promptOverrideConfiguration"></a>
 Contains configurations to override prompt templates in different parts of an inline collaborator sequence. For more information, see [Advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html).   
Type: [PromptOverrideConfiguration](API_agent-runtime_PromptOverrideConfiguration.md) object  
Required: No

## See Also
<a name="API_agent-runtime_Collaborator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/Collaborator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/Collaborator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/Collaborator) 