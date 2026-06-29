

# SystemContentBlock
<a name="API_agent_SystemContentBlock"></a>

Contains a system prompt to provide context to the model or to describe how it should behave. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html).

## Contents
<a name="API_agent_SystemContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cachePoint **   <a name="bedrock-Type-agent_SystemContentBlock-cachePoint"></a>
Creates a cache checkpoint within a tool designation  
Type: [CachePointBlock](API_agent_CachePointBlock.md) object  
Required: No

 ** text **   <a name="bedrock-Type-agent_SystemContentBlock-text"></a>
The text in the system prompt.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## See Also
<a name="API_agent_SystemContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/SystemContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/SystemContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/SystemContentBlock) 