

# S3Identifier
<a name="API_agent-runtime_S3Identifier"></a>

 The identifier information for an Amazon S3 bucket. 

## Contents
<a name="API_agent-runtime_S3Identifier_Contents"></a>

 ** s3BucketName **   <a name="bedrock-Type-agent-runtime_S3Identifier-s3BucketName"></a>
 The name of the S3 bucket.   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`   
Required: No

 ** s3ObjectKey **   <a name="bedrock-Type-agent-runtime_S3Identifier-s3ObjectKey"></a>
 The S3 object key for the S3 resource.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[\.\-\!\*\_\'\(\)a-zA-Z0-9][\.\-\!\*\_\'\(\)\/a-zA-Z0-9]*`   
Required: No

## See Also
<a name="API_agent-runtime_S3Identifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/S3Identifier) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/S3Identifier) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/S3Identifier) 