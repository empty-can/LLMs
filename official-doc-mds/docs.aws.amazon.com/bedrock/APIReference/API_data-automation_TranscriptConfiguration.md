

# TranscriptConfiguration
<a name="API_data-automation_TranscriptConfiguration"></a>

Configuration for transcript options. This option allows you to enable speaker labeling and channel labeling.

## Contents
<a name="API_data-automation_TranscriptConfiguration_Contents"></a>

 ** channelLabeling **   <a name="bedrock-Type-data-automation_TranscriptConfiguration-channelLabeling"></a>
Enables channel labeling. Each audio channel will be labeled with a number, and the transcript will indicate which channel is being used.  
Type: [ChannelLabelingConfiguration](API_data-automation_ChannelLabelingConfiguration.md) object  
Required: No

 ** speakerLabeling **   <a name="bedrock-Type-data-automation_TranscriptConfiguration-speakerLabeling"></a>
Enables speaker labeling. Each speaker within a transcript will recieve a number, and the transcript will note which speaker is talking.  
Type: [SpeakerLabelingConfiguration](API_data-automation_SpeakerLabelingConfiguration.md) object  
Required: No

## See Also
<a name="API_data-automation_TranscriptConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/TranscriptConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/TranscriptConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/TranscriptConfiguration) 