

# PromptTemplateConfiguration
<a name="API_agent_PromptTemplateConfiguration"></a>

Contains the message for a prompt. For more information, see [Construct and store reusable prompts with Prompt management in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html).

## Contents
<a name="API_agent_PromptTemplateConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** chat **   <a name="bedrock-Type-agent_PromptTemplateConfiguration-chat"></a>
Contains configurations to use the prompt in a conversational format.  
Type: [ChatPromptTemplateConfiguration](API_agent_ChatPromptTemplateConfiguration.md) object  
Required: No

 ** text **   <a name="bedrock-Type-agent_PromptTemplateConfiguration-text"></a>
Contains configurations for the text in a message for a prompt.  
Type: [TextPromptTemplateConfiguration](API_agent_TextPromptTemplateConfiguration.md) object  
Required: No

## See Also
<a name="API_agent_PromptTemplateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PromptTemplateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PromptTemplateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PromptTemplateConfiguration) 