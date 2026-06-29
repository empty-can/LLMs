

# ReasoningTextBlock
<a name="API_agent-runtime_ReasoningTextBlock"></a>

Contains information about the reasoning that the model used to return the content in the content block.

## Contents
<a name="API_agent-runtime_ReasoningTextBlock_Contents"></a>

 ** text **   <a name="bedrock-Type-agent-runtime_ReasoningTextBlock-text"></a>
Text describing the reasoning that the model used to return the content in the content block.  
Type: String  
Required: Yes

 ** signature **   <a name="bedrock-Type-agent-runtime_ReasoningTextBlock-signature"></a>
A hash of all the messages in the conversation to ensure that the content in the reasoning text block isn't tampered with. You must submit the signature in subsequent `Converse` requests, in addition to the previous messages. If the previous messages are tampered with, the response throws an error.  
Type: String  
Required: No

## See Also
<a name="API_agent-runtime_ReasoningTextBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ReasoningTextBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ReasoningTextBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ReasoningTextBlock) 