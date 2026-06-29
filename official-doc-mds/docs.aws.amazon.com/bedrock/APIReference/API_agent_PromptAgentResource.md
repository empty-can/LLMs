

# PromptAgentResource
<a name="API_agent_PromptAgentResource"></a>

Contains specifications for an Amazon Bedrock agent with which to use the prompt. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) and [Automate tasks in your application using conversational agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html).

## Contents
<a name="API_agent_PromptAgentResource_Contents"></a>

 ** agentIdentifier **   <a name="bedrock-Type-agent_PromptAgentResource-agentIdentifier"></a>
The ARN of the agent with which to use the prompt.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}`   
Required: Yes

## See Also
<a name="API_agent_PromptAgentResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PromptAgentResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PromptAgentResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PromptAgentResource) 