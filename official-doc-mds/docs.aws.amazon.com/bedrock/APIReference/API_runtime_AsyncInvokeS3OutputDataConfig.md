

# AsyncInvokeS3OutputDataConfig
<a name="API_runtime_AsyncInvokeS3OutputDataConfig"></a>

Asynchronous invocation output data settings.

## Contents
<a name="API_runtime_AsyncInvokeS3OutputDataConfig_Contents"></a>

 ** s3Uri **   <a name="bedrock-Type-runtime_AsyncInvokeS3OutputDataConfig-s3Uri"></a>
An object URI starting with `s3://`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: Yes

 ** bucketOwner **   <a name="bedrock-Type-runtime_AsyncInvokeS3OutputDataConfig-bucketOwner"></a>
If the bucket belongs to another AWS account, specify that account's ID.  
Type: String  
Pattern: `[0-9]{12}`   
Required: No

 ** kmsKeyId **   <a name="bedrock-Type-runtime_AsyncInvokeS3OutputDataConfig-kmsKeyId"></a>
A KMS encryption key ID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:((key/[a-zA-Z0-9-]{36})|(alias/[a-zA-Z0-9-_/]+))`   
Required: No

## See Also
<a name="API_runtime_AsyncInvokeS3OutputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/AsyncInvokeS3OutputDataConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/AsyncInvokeS3OutputDataConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/AsyncInvokeS3OutputDataConfig) 