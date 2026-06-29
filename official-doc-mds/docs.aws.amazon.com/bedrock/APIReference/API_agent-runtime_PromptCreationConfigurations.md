

# PromptCreationConfigurations
<a name="API_agent-runtime_PromptCreationConfigurations"></a>

Specifies parameters that control how the service populates the agent prompt for an `InvokeAgent` or `InvokeInlineAgent` request. You can control which aspects of previous invocations in the same agent session the service uses to populate the agent prompt. This gives you more granular control over the contextual history that is used to process the current request.

## Contents
<a name="API_agent-runtime_PromptCreationConfigurations_Contents"></a>

 ** excludePreviousThinkingSteps **   <a name="bedrock-Type-agent-runtime_PromptCreationConfigurations-excludePreviousThinkingSteps"></a>
If `true`, the service removes any content between `<thinking>` tags from previous conversations in an agent session. The service will only remove content from already processed turns. This helps you remove content which might not be useful for current and subsequent invocations. This can reduce the input token count and potentially save costs. The default value is `false`.  
Type: Boolean  
Required: No

 ** previousConversationTurnsToInclude **   <a name="bedrock-Type-agent-runtime_PromptCreationConfigurations-previousConversationTurnsToInclude"></a>
The number of previous conversations from the ongoing agent session to include in the conversation history of the agent prompt, during the current invocation. This gives you more granular control over the context that the model is made aware of, and helps the model remove older context which is no longer useful during the ongoing agent session.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_agent-runtime_PromptCreationConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/PromptCreationConfigurations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/PromptCreationConfigurations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/PromptCreationConfigurations) 