

# AudioSegment
<a name="API_agent-runtime_AudioSegment"></a>

Contains information about an audio segment retrieved from a knowledge base, including its location and transcription.

This data type is used in the following API operations:
+  [Retrieve response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html#API_agent-runtime_Retrieve_ResponseSyntax) – in the `audio` field

## Contents
<a name="API_agent-runtime_AudioSegment_Contents"></a>

 ** s3Uri **   <a name="bedrock-Type-agent-runtime_AudioSegment-s3Uri"></a>
The S3 URI where this specific audio segment is stored in the multimodal storage destination.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** transcription **   <a name="bedrock-Type-agent-runtime_AudioSegment-transcription"></a>
The text transcription of the audio segment content.  
Type: String  
Required: No

## See Also
<a name="API_agent-runtime_AudioSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AudioSegment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AudioSegment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AudioSegment) 