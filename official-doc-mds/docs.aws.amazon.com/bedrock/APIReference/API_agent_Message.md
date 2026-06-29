

# Message
<a name="API_agent_Message"></a>

A message input or response from a model. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html).

## Contents
<a name="API_agent_Message_Contents"></a>

 ** content **   <a name="bedrock-Type-agent_Message-content"></a>
The content in the message.  
Type: Array of [ContentBlock](API_agent_ContentBlock.md) objects  
Required: Yes

 ** role **   <a name="bedrock-Type-agent_Message-role"></a>
The role that the message belongs to.  
Type: String  
Valid Values: `user | assistant`   
Required: Yes

## See Also
<a name="API_agent_Message_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/Message) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/Message) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/Message) 