

# TextPromptTemplateConfiguration
<a name="API_agent_TextPromptTemplateConfiguration"></a>

Contains configurations for a text prompt template. To include a variable, enclose a word in double curly braces as in `{{variable}}`.

## Contents
<a name="API_agent_TextPromptTemplateConfiguration_Contents"></a>

 ** text **   <a name="bedrock-Type-agent_TextPromptTemplateConfiguration-text"></a>
The message for the prompt.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** cachePoint **   <a name="bedrock-Type-agent_TextPromptTemplateConfiguration-cachePoint"></a>
A cache checkpoint within a template configuration.  
Type: [CachePointBlock](API_agent_CachePointBlock.md) object  
Required: No

 ** inputVariables **   <a name="bedrock-Type-agent_TextPromptTemplateConfiguration-inputVariables"></a>
An array of the variables in the prompt template.  
Type: Array of [PromptInputVariable](API_agent_PromptInputVariable.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 20 items.  
Required: No

## See Also
<a name="API_agent_TextPromptTemplateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/TextPromptTemplateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/TextPromptTemplateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/TextPromptTemplateConfiguration) 