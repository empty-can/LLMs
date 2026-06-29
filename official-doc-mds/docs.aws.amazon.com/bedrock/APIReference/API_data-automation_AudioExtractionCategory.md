

# AudioExtractionCategory
<a name="API_data-automation_AudioExtractionCategory"></a>

Settings for generating data from audio.

## Contents
<a name="API_data-automation_AudioExtractionCategory_Contents"></a>

 ** state **   <a name="bedrock-Type-data-automation_AudioExtractionCategory-state"></a>
Whether generating categorical data from audio is enabled.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

 ** typeConfiguration **   <a name="bedrock-Type-data-automation_AudioExtractionCategory-typeConfiguration"></a>
This element contains information about extractions from different types. Used to enable speaker and channel labeling for transcripts.  
Type: [AudioExtractionCategoryTypeConfiguration](API_data-automation_AudioExtractionCategoryTypeConfiguration.md) object  
Required: No

 ** types **   <a name="bedrock-Type-data-automation_AudioExtractionCategory-types"></a>
The types of data to generate.  
Type: Array of strings  
Valid Values: `AUDIO_CONTENT_MODERATION | TRANSCRIPT | TOPIC_CONTENT_MODERATION`   
Required: No

## See Also
<a name="API_data-automation_AudioExtractionCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/AudioExtractionCategory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/AudioExtractionCategory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/AudioExtractionCategory) 