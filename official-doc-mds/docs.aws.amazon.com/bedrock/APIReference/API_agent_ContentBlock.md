

# ContentBlock
<a name="API_agent_ContentBlock"></a>

Contains the content for the message you pass to, or receive from a model. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html).

## Contents
<a name="API_agent_ContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cachePoint **   <a name="bedrock-Type-agent_ContentBlock-cachePoint"></a>
Creates a cache checkpoint within a message.  
Type: [CachePointBlock](API_agent_CachePointBlock.md) object  
Required: No

 ** text **   <a name="bedrock-Type-agent_ContentBlock-text"></a>
The text in the message.  
Type: String  
Required: No

## See Also
<a name="API_agent_ContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ContentBlock) 