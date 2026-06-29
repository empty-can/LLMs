

# ChatPromptTemplateConfiguration
<a name="API_agent_ChatPromptTemplateConfiguration"></a>

Contains configurations to use a prompt in a conversational format. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html).

## Contents
<a name="API_agent_ChatPromptTemplateConfiguration_Contents"></a>

 ** messages **   <a name="bedrock-Type-agent_ChatPromptTemplateConfiguration-messages"></a>
Contains messages in the chat for the prompt.  
Type: Array of [Message](API_agent_Message.md) objects  
Required: Yes

 ** inputVariables **   <a name="bedrock-Type-agent_ChatPromptTemplateConfiguration-inputVariables"></a>
An array of the variables in the prompt template.  
Type: Array of [PromptInputVariable](API_agent_PromptInputVariable.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 20 items.  
Required: No

 ** system **   <a name="bedrock-Type-agent_ChatPromptTemplateConfiguration-system"></a>
Contains system prompts to provide context to the model or to describe how it should behave.  
Type: Array of [SystemContentBlock](API_agent_SystemContentBlock.md) objects  
Required: No

 ** toolConfiguration **   <a name="bedrock-Type-agent_ChatPromptTemplateConfiguration-toolConfiguration"></a>
Configuration information for the tools that the model can use when generating a response.  
Type: [ToolConfiguration](API_agent_ToolConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_ChatPromptTemplateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ChatPromptTemplateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ChatPromptTemplateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ChatPromptTemplateConfiguration) 