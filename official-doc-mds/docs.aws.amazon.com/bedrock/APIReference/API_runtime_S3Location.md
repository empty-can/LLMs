

# S3Location
<a name="API_runtime_S3Location"></a>

A storage location in an Amazon S3 bucket.

## Contents
<a name="API_runtime_S3Location_Contents"></a>

 ** uri **   <a name="bedrock-Type-runtime_S3Location-uri"></a>
An object URI starting with `s3://`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: Yes

 ** bucketOwner **   <a name="bedrock-Type-runtime_S3Location-bucketOwner"></a>
If the bucket belongs to another AWS account, specify that account's ID.  
Type: String  
Pattern: `[0-9]{12}`   
Required: No

## See Also
<a name="API_runtime_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/S3Location) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/S3Location) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/S3Location) 