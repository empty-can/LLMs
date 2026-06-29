

# PromptTemplate
<a name="API_agent-runtime_PromptTemplate"></a>

Contains the template for the prompt that's sent to the model for response generation. For more information, see [Knowledge base prompt templates](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html#kb-test-config-sysprompt).

This data type is used in the following API operations:
+  [RetrieveAndGenerate request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_RequestSyntax) – in the `filter` field

## Contents
<a name="API_agent-runtime_PromptTemplate_Contents"></a>

 ** textPromptTemplate **   <a name="bedrock-Type-agent-runtime_PromptTemplate-textPromptTemplate"></a>
The template for the prompt that's sent to the model for response generation. You can include prompt placeholders, which become replaced before the prompt is sent to the model to provide instructions and context to the model. In addition, you can include XML tags to delineate meaningful sections of the prompt template.  
For more information, see the following resources:  
+  [Knowledge base prompt templates](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html#kb-test-config-sysprompt) 
+  [Use XML tags with Anthropic Claude models](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags) 
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4000.  
Required: No

## See Also
<a name="API_agent-runtime_PromptTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/PromptTemplate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/PromptTemplate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/PromptTemplate) 