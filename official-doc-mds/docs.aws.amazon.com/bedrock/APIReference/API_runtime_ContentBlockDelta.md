

# ContentBlockDelta
<a name="API_runtime_ContentBlockDelta"></a>

A block of content in a streaming response.

## Contents
<a name="API_runtime_ContentBlockDelta_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** citation **   <a name="bedrock-Type-runtime_ContentBlockDelta-citation"></a>
Incremental citation information that is streamed as part of the response generation process.  
Type: [CitationsDelta](API_runtime_CitationsDelta.md) object  
Required: No

 ** image **   <a name="bedrock-Type-runtime_ContentBlockDelta-image"></a>
A streaming delta event containing incremental image data.  
Type: [ImageBlockDelta](API_runtime_ImageBlockDelta.md) object  
Required: No

 ** reasoningContent **   <a name="bedrock-Type-runtime_ContentBlockDelta-reasoningContent"></a>
Contains content regarding the reasoning that is carried out by the model. Reasoning refers to a Chain of Thought (CoT) that the model generates to enhance the accuracy of its final response.  
Type: [ReasoningContentBlockDelta](API_runtime_ReasoningContentBlockDelta.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** text **   <a name="bedrock-Type-runtime_ContentBlockDelta-text"></a>
The content text.  
Type: String  
Required: No

 ** toolResult **   <a name="bedrock-Type-runtime_ContentBlockDelta-toolResult"></a>
An incremental update that contains the results from a tool call.  
Type: Array of [ToolResultBlockDelta](API_runtime_ToolResultBlockDelta.md) objects  
Required: No

 ** toolUse **   <a name="bedrock-Type-runtime_ContentBlockDelta-toolUse"></a>
Information about a tool that the model is requesting to use.  
Type: [ToolUseBlockDelta](API_runtime_ToolUseBlockDelta.md) object  
Required: No

## See Also
<a name="API_runtime_ContentBlockDelta_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ContentBlockDelta) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ContentBlockDelta) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ContentBlockDelta) 