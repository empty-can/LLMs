

# LoggingConfig
<a name="API_LoggingConfig"></a>

Configuration fields for invocation logging.

## Contents
<a name="API_LoggingConfig_Contents"></a>

 ** audioDataDeliveryEnabled **   <a name="bedrock-Type-LoggingConfig-audioDataDeliveryEnabled"></a>
Set to include audio data in the log delivery.  
Type: Boolean  
Required: No

 ** cloudWatchConfig **   <a name="bedrock-Type-LoggingConfig-cloudWatchConfig"></a>
CloudWatch logging configuration.  
Type: [CloudWatchConfig](API_CloudWatchConfig.md) object  
Required: No

 ** embeddingDataDeliveryEnabled **   <a name="bedrock-Type-LoggingConfig-embeddingDataDeliveryEnabled"></a>
Set to include embeddings data in the log delivery.  
Type: Boolean  
Required: No

 ** imageDataDeliveryEnabled **   <a name="bedrock-Type-LoggingConfig-imageDataDeliveryEnabled"></a>
Set to include image data in the log delivery.  
Type: Boolean  
Required: No

 ** s3Config **   <a name="bedrock-Type-LoggingConfig-s3Config"></a>
S3 configuration for storing log data.  
Type: [S3Config](API_S3Config.md) object  
Required: No

 ** textDataDeliveryEnabled **   <a name="bedrock-Type-LoggingConfig-textDataDeliveryEnabled"></a>
Set to include text data in the log delivery.  
Type: Boolean  
Required: No

 ** videoDataDeliveryEnabled **   <a name="bedrock-Type-LoggingConfig-videoDataDeliveryEnabled"></a>
Set to include video data in the log delivery.  
Type: Boolean  
Required: No

## See Also
<a name="API_LoggingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/LoggingConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/LoggingConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/LoggingConfig) 