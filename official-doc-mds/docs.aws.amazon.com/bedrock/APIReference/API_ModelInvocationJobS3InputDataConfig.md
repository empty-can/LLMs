

# ModelInvocationJobS3InputDataConfig
<a name="API_ModelInvocationJobS3InputDataConfig"></a>

Contains the configuration of the S3 location of the input data.

## Contents
<a name="API_ModelInvocationJobS3InputDataConfig_Contents"></a>

 ** s3Uri **   <a name="bedrock-Type-ModelInvocationJobS3InputDataConfig-s3Uri"></a>
The S3 location of the input data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `s3://[a-z0-9][-.a-z0-9]{1,61}[a-z0-9](?:/[-!_*'().a-z0-9A-Z]+(?:/[-!_*'().a-z0-9A-Z]+)*)?/?`   
Required: Yes

 ** s3BucketOwner **   <a name="bedrock-Type-ModelInvocationJobS3InputDataConfig-s3BucketOwner"></a>
The ID of the AWS account that owns the S3 bucket containing the input data.  
Type: String  
Pattern: `[0-9]{12}`   
Required: No

 ** s3InputFormat **   <a name="bedrock-Type-ModelInvocationJobS3InputDataConfig-s3InputFormat"></a>
The format of the input data.  
Type: String  
Valid Values: `JSONL`   
Required: No

## See Also
<a name="API_ModelInvocationJobS3InputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ModelInvocationJobS3InputDataConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ModelInvocationJobS3InputDataConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ModelInvocationJobS3InputDataConfig) 