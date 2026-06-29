

# AudioBlock
<a name="API_runtime_AudioBlock"></a>

An audio content block that contains audio data in various supported formats.

## Contents
<a name="API_runtime_AudioBlock_Contents"></a>

 ** format **   <a name="bedrock-Type-runtime_AudioBlock-format"></a>
The format of the audio data, such as MP3, WAV, FLAC, or other supported audio formats.  
Type: String  
Valid Values: `mp3 | opus | wav | aac | flac | mp4 | ogg | mkv | mka | x-aac | m4a | mpeg | mpga | pcm | webm`   
Required: Yes

 ** source **   <a name="bedrock-Type-runtime_AudioBlock-source"></a>
The source of the audio data, which can be provided as raw bytes or an S3 location.  
Type: [AudioSource](API_runtime_AudioSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** error **   <a name="bedrock-Type-runtime_AudioBlock-error"></a>
Error information if the audio block could not be processed or contains invalid data.  
Type: [ErrorBlock](API_runtime_ErrorBlock.md) object  
Required: No

## See Also
<a name="API_runtime_AudioBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/AudioBlock) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/AudioBlock) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/AudioBlock) 