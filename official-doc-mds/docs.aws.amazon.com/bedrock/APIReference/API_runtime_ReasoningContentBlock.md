

# ReasoningContentBlock
<a name="API_runtime_ReasoningContentBlock"></a>

Contains content regarding the reasoning that is carried out by the model with respect to the content in the content block. Reasoning refers to a Chain of Thought (CoT) that the model generates to enhance the accuracy of its final response.

## Contents
<a name="API_runtime_ReasoningContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** reasoningText **   <a name="bedrock-Type-runtime_ReasoningContentBlock-reasoningText"></a>
The reasoning that the model used to return the output.  
Type: [ReasoningTextBlock](API_runtime_ReasoningTextBlock.md) object  
Required: No

 ** redactedContent **   <a name="bedrock-Type-runtime_ReasoningContentBlock-redactedContent"></a>
The content in the reasoning that was encrypted by the model provider for safety reasons. The encryption doesn't affect the quality of responses.  
Type: Base64-encoded binary data object  
Required: No

## See Also
<a name="API_runtime_ReasoningContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ReasoningContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ReasoningContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ReasoningContentBlock) 