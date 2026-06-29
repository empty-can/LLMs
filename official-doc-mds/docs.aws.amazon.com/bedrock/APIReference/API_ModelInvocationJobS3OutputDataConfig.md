

# ModelInvocationJobS3OutputDataConfig
<a name="API_ModelInvocationJobS3OutputDataConfig"></a>

Contains the configuration of the S3 location of the output data.

## Contents
<a name="API_ModelInvocationJobS3OutputDataConfig_Contents"></a>

 ** s3Uri **   <a name="bedrock-Type-ModelInvocationJobS3OutputDataConfig-s3Uri"></a>
The S3 location of the output data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `s3://[a-z0-9][-.a-z0-9]{1,61}[a-z0-9](?:/[-!_*'().a-z0-9A-Z]+(?:/[-!_*'().a-z0-9A-Z]+)*)?/?`   
Required: Yes

 ** s3BucketOwner **   <a name="bedrock-Type-ModelInvocationJobS3OutputDataConfig-s3BucketOwner"></a>
The ID of the AWS account that owns the S3 bucket containing the output data.  
Type: String  
Pattern: `[0-9]{12}`   
Required: No

 ** s3EncryptionKeyId **   <a name="bedrock-Type-ModelInvocationJobS3OutputDataConfig-s3EncryptionKeyId"></a>
The unique identifier of the key that encrypts the S3 location of the output data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)))|([a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+)`   
Required: No

## See Also
<a name="API_ModelInvocationJobS3OutputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ModelInvocationJobS3OutputDataConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ModelInvocationJobS3OutputDataConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ModelInvocationJobS3OutputDataConfig) 