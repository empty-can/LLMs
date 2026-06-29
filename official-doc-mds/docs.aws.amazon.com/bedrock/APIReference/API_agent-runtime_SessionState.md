

# SessionState
<a name="API_agent-runtime_SessionState"></a>

Contains parameters that specify various attributes that persist across a session or prompt. You can define session state attributes as key-value pairs when writing a [Lambda function](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html) for an action group or pass them when making an [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html) request. Use session state attributes to control and provide conversational context for your agent and to help customize your agent's behavior. For more information, see [Control session context](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html).

## Contents
<a name="API_agent-runtime_SessionState_Contents"></a>

 ** conversationHistory **   <a name="bedrock-Type-agent-runtime_SessionState-conversationHistory"></a>
The state's conversation history.  
Type: [ConversationHistory](API_agent-runtime_ConversationHistory.md) object  
Required: No

 ** files **   <a name="bedrock-Type-agent-runtime_SessionState-files"></a>
Contains information about the files used by code interpreter.  
Type: Array of [InputFile](API_agent-runtime_InputFile.md) objects  
Required: No

 ** invocationId **   <a name="bedrock-Type-agent-runtime_SessionState-invocationId"></a>
The identifier of the invocation of an action. This value must match the `invocationId` returned in the `InvokeAgent` response for the action whose results are provided in the `returnControlInvocationResults` field. For more information, see [Return control to the agent developer](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html) and [Control session context](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html).  
Type: String  
Required: No

 ** knowledgeBaseConfigurations **   <a name="bedrock-Type-agent-runtime_SessionState-knowledgeBaseConfigurations"></a>
An array of configurations, each of which applies to a knowledge base attached to the agent.  
Type: Array of [KnowledgeBaseConfiguration](API_agent-runtime_KnowledgeBaseConfiguration.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

 ** promptSessionAttributes **   <a name="bedrock-Type-agent-runtime_SessionState-promptSessionAttributes"></a>
Contains attributes that persist across a prompt and the values of those attributes.   
+ In orchestration prompt template, these attributes replace the $prompt\_session\_attributes$ placeholder variable. For more information, see [Prompt template placeholder variables](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-placeholders.html).
+ In [multi-agent collaboration](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html), the `promptSessionAttributes` will only be used by supervisor agent when $prompt\_session\_attributes$ is present in prompt template. 
Type: String to string map  
Required: No

 ** returnControlInvocationResults **   <a name="bedrock-Type-agent-runtime_SessionState-returnControlInvocationResults"></a>
Contains information about the results from the action group invocation. For more information, see [Return control to the agent developer](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html) and [Control session context](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html).  
If you include this field, the `inputText` field will be ignored.
Type: Array of [InvocationResultMember](API_agent-runtime_InvocationResultMember.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Required: No

 ** sessionAttributes **   <a name="bedrock-Type-agent-runtime_SessionState-sessionAttributes"></a>
Contains attributes that persist across a session and the values of those attributes. If `sessionAttributes` are passed to a supervisor agent in [multi-agent collaboration](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html), it will be forwarded to all agent collaborators.  
Type: String to string map  
Required: No

## See Also
<a name="API_agent-runtime_SessionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/SessionState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/SessionState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/SessionState) 