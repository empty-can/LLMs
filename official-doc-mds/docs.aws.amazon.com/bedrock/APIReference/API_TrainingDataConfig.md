

# TrainingDataConfig
<a name="API_TrainingDataConfig"></a>

S3 Location of the training data.

## Contents
<a name="API_TrainingDataConfig_Contents"></a>

 ** invocationLogsConfig **   <a name="bedrock-Type-TrainingDataConfig-invocationLogsConfig"></a>
Settings for using invocation logs to customize a model.  
Type: [InvocationLogsConfig](API_InvocationLogsConfig.md) object  
Required: No

 ** s3Uri **   <a name="bedrock-Type-TrainingDataConfig-s3Uri"></a>
The S3 URI where the training data is stored.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `s3://[a-z0-9][-.a-z0-9]{1,61}[a-z0-9](?:/[-!_*'().a-z0-9A-Z]+(?:/[-!_*'().a-z0-9A-Z]+)*)?/?`   
Required: No

## See Also
<a name="API_TrainingDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/TrainingDataConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/TrainingDataConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/TrainingDataConfig) 