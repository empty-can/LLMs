

# AudioSegmentationConfiguration
<a name="API_agent_AudioSegmentationConfiguration"></a>

Configuration for segmenting audio content during multimodal knowledge base ingestion. Determines how audio files are divided into chunks for processing.

## Contents
<a name="API_agent_AudioSegmentationConfiguration_Contents"></a>

 ** fixedLengthDuration **   <a name="bedrock-Type-agent_AudioSegmentationConfiguration-fixedLengthDuration"></a>
The duration in seconds for each audio segment. Audio files will be divided into chunks of this length for processing.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 30.  
Required: Yes

## See Also
<a name="API_agent_AudioSegmentationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/AudioSegmentationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/AudioSegmentationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/AudioSegmentationConfiguration) 