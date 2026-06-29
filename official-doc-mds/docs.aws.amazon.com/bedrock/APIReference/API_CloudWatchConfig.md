

# CloudWatchConfig
<a name="API_CloudWatchConfig"></a>

CloudWatch logging configuration.

## Contents
<a name="API_CloudWatchConfig_Contents"></a>

 ** logGroupName **   <a name="bedrock-Type-CloudWatchConfig-logGroupName"></a>
The log group name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: Yes

 ** roleArn **   <a name="bedrock-Type-CloudWatchConfig-roleArn"></a>
The role Amazon Resource Name (ARN).  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** largeDataDeliveryS3Config **   <a name="bedrock-Type-CloudWatchConfig-largeDataDeliveryS3Config"></a>
S3 configuration for delivering a large amount of data.  
Type: [S3Config](API_S3Config.md) object  
Required: No

## See Also
<a name="API_CloudWatchConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CloudWatchConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CloudWatchConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CloudWatchConfig) 