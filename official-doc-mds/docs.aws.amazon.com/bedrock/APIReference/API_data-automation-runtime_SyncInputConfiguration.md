

# SyncInputConfiguration
<a name="API_data-automation-runtime_SyncInputConfiguration"></a>

Input configuration for a synchronous data automation invocation.

## Contents
<a name="API_data-automation-runtime_SyncInputConfiguration_Contents"></a>

 ** bytes **   <a name="bedrock-Type-data-automation-runtime_SyncInputConfiguration-bytes"></a>
The raw bytes of the input asset.  
Type: Base64-encoded binary data object  
Required: No

 ** s3Uri **   <a name="bedrock-Type-data-automation-runtime_SyncInputConfiguration-s3Uri"></a>
The S3 URI of the input asset.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/[^\x00-\x1F\x7F\{^}%`\]">\[~<#|]*)?`   
Required: No

## See Also
<a name="API_data-automation-runtime_SyncInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/SyncInputConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/SyncInputConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/SyncInputConfiguration) 