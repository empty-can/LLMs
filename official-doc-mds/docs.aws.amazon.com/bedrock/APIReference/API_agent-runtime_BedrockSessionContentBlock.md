

# BedrockSessionContentBlock
<a name="API_agent-runtime_BedrockSessionContentBlock"></a>

A block of content that you pass to, or receive from, a Amazon Bedrock session in an invocation step. You pass the content to a session in the `payLoad` of the [PutInvocationStep](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_PutInvocationStep.html) API operation. You retrieve the content with the [GetInvocationStep](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetInvocationStep.html) API operation.

For more information about sessions, see [Store and retrieve conversation history and context with Amazon Bedrock sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html).

## Contents
<a name="API_agent-runtime_BedrockSessionContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** image **   <a name="bedrock-Type-agent-runtime_BedrockSessionContentBlock-image"></a>
The image in the invocation step.  
Type: [ImageBlock](API_agent-runtime_ImageBlock.md) object  
Required: No

 ** text **   <a name="bedrock-Type-agent-runtime_BedrockSessionContentBlock-text"></a>
The text in the invocation step.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## See Also
<a name="API_agent-runtime_BedrockSessionContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/BedrockSessionContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/BedrockSessionContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/BedrockSessionContentBlock) 