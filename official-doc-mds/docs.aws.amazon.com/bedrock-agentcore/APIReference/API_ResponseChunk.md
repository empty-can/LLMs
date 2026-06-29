

# ResponseChunk
<a name="API_ResponseChunk"></a>

A structure representing a response chunk that contains exactly one of the possible event types: `contentStart`, `contentDelta`, or `contentStop`.

## Contents
<a name="API_ResponseChunk_Contents"></a>

 ** contentDelta **   <a name="BedrockAgentCore-Type-ResponseChunk-contentDelta"></a>
An event containing incremental output (stdout or stderr) from the command execution. These are the middle chunks.  
Type: [ContentDeltaEvent](API_ContentDeltaEvent.md) object  
Required: No

 ** contentStart **   <a name="BedrockAgentCore-Type-ResponseChunk-contentStart"></a>
An event indicating the start of content streaming from the command execution. This is the first chunk received.  
Type: [ContentStartEvent](API_ContentStartEvent.md) object  
Required: No

 ** contentStop **   <a name="BedrockAgentCore-Type-ResponseChunk-contentStop"></a>
An event indicating the completion of the command execution, including the exit code and final status. This is the last chunk received.  
Type: [ContentStopEvent](API_ContentStopEvent.md) object  
Required: No

## See Also
<a name="API_ResponseChunk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ResponseChunk) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ResponseChunk) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ResponseChunk) 