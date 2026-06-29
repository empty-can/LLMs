

# ContentBlock
<a name="API_runtime_ContentBlock"></a>

A block of content for a message that you pass to, or receive from, a model with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) API operations.

## Contents
<a name="API_runtime_ContentBlock_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** audio **   <a name="bedrock-Type-runtime_ContentBlock-audio"></a>
An audio content block containing audio data in the conversation.  
Type: [AudioBlock](API_runtime_AudioBlock.md) object  
Required: No

 ** cachePoint **   <a name="bedrock-Type-runtime_ContentBlock-cachePoint"></a>
CachePoint to include in the message.  
Type: [CachePointBlock](API_runtime_CachePointBlock.md) object  
Required: No

 ** citationsContent **   <a name="bedrock-Type-runtime_ContentBlock-citationsContent"></a>
A content block that contains both generated text and associated citation information, providing traceability between the response and source documents.  
Type: [CitationsContentBlock](API_runtime_CitationsContentBlock.md) object  
Required: No

 ** document **   <a name="bedrock-Type-runtime_ContentBlock-document"></a>
A document to include in the message.  
Type: [DocumentBlock](API_runtime_DocumentBlock.md) object  
Required: No

 ** guardContent **   <a name="bedrock-Type-runtime_ContentBlock-guardContent"></a>
Contains the content to assess with the guardrail. If you don't specify `guardContent` in a call to the Converse API, the guardrail (if passed in the Converse API) assesses the entire message.  
For more information, see [Use a guardrail with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-converse-api.html).  
Type: [GuardrailConverseContentBlock](API_runtime_GuardrailConverseContentBlock.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** image **   <a name="bedrock-Type-runtime_ContentBlock-image"></a>
Image to include in the message.   
This field is only supported by Anthropic Claude 3 models.
Type: [ImageBlock](API_runtime_ImageBlock.md) object  
Required: No

 ** reasoningContent **   <a name="bedrock-Type-runtime_ContentBlock-reasoningContent"></a>
Contains content regarding the reasoning that is carried out by the model. Reasoning refers to a Chain of Thought (CoT) that the model generates to enhance the accuracy of its final response.  
Type: [ReasoningContentBlock](API_runtime_ReasoningContentBlock.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** searchResult **   <a name="bedrock-Type-runtime_ContentBlock-searchResult"></a>
Search result to include in the message.  
Type: [SearchResultBlock](API_runtime_SearchResultBlock.md) object  
Required: No

 ** text **   <a name="bedrock-Type-runtime_ContentBlock-text"></a>
Text to include in the message.  
Type: String  
Required: No

 ** toolResult **   <a name="bedrock-Type-runtime_ContentBlock-toolResult"></a>
The result for a tool request that a model makes.  
Type: [ToolResultBlock](API_runtime_ToolResultBlock.md) object  
Required: No

 ** toolUse **   <a name="bedrock-Type-runtime_ContentBlock-toolUse"></a>
Information about a tool use request from a model.  
Type: [ToolUseBlock](API_runtime_ToolUseBlock.md) object  
Required: No

 ** video **   <a name="bedrock-Type-runtime_ContentBlock-video"></a>
Video to include in the message.   
Type: [VideoBlock](API_runtime_VideoBlock.md) object  
Required: No

## See Also
<a name="API_runtime_ContentBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ContentBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ContentBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ContentBlock) 