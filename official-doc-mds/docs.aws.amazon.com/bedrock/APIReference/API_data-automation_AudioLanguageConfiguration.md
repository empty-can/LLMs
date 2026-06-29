

# AudioLanguageConfiguration
<a name="API_data-automation_AudioLanguageConfiguration"></a>

This allows you to set the input and output language of your audio. The input language can be set to any of the languages supported by Bedrock Data Automation. The output can either be set to english or whatever the dominant language is of the audio, determined by the language spoken for the most seconds.

## Contents
<a name="API_data-automation_AudioLanguageConfiguration_Contents"></a>

 ** generativeOutputLanguage **   <a name="bedrock-Type-data-automation_AudioLanguageConfiguration-generativeOutputLanguage"></a>
The output language of your processing results. This can either be set to `EN` (English) or `DEFAULT` which will output the results in the dominant language of the audio. The dominant language is determined as the language in the audio, spoken the longest in the input audio.  
Type: String  
Valid Values: `DEFAULT | EN`   
Required: No

 ** identifyMultipleLanguages **   <a name="bedrock-Type-data-automation_AudioLanguageConfiguration-identifyMultipleLanguages"></a>
The toggle determining if you want to detect multiple languages from your audio.  
Type: Boolean  
Required: No

 ** inputLanguages **   <a name="bedrock-Type-data-automation_AudioLanguageConfiguration-inputLanguages"></a>
The input language of your audio. This can be set to any of the currently supported languages via the language codes.  
Type: Array of strings  
Valid Values: `EN | DE | ES | FR | IT | PT | JA | KO | CN | TW | HK`   
Required: No

## See Also
<a name="API_data-automation_AudioLanguageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/AudioLanguageConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/AudioLanguageConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/AudioLanguageConfiguration) 